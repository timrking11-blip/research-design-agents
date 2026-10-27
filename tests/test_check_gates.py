import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_gates  # noqa: E402

GOOD = {"signed_by": "Owner", "signed_on": "2026-10-14", "check": "read every success measure"}


class GateTests(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        for name in ("gates.yaml", "PROBLEM.md"):
            shutil.copy(ROOT / name, self.dir / name)
        for name in ("agents", "skills", "schemas"):
            (self.dir / name).mkdir()
            (self.dir / name / "README.md").write_text("readme")

    def tearDown(self):
        shutil.rmtree(self.dir)

    def sign(self, *ids, **override):
        path = self.dir / "gates.yaml"
        config = yaml.safe_load(path.read_text())
        for gate in config["gates"]:
            if gate["id"] in ids:
                gate.update(GOOD, **override)
        path.write_text(yaml.safe_dump(config, sort_keys=False))

    def confirm_problem(self):
        path = self.dir / "PROBLEM.md"
        path.write_text(path.read_text().replace("Status: DRAFT", "Status: CONFIRMED"))

    def add_eval(self):
        (self.dir / "evals" / "case-one").mkdir(parents=True)
        (self.dir / "evals" / "case-one" / "prompt.md").write_text("task")

    def errors(self):
        return check_gates.check(self.dir)[0]

    def test_template_as_shipped_passes(self):
        self.assertEqual(self.errors(), [])

    def test_repository_itself_passes(self):
        self.assertEqual(check_gates.check(ROOT)[0], [])

    def test_build_before_gates_fails(self):
        (self.dir / "skills" / "x").mkdir()
        (self.dir / "skills" / "x" / "SKILL.md").write_text("skill")
        errors = self.errors()
        self.assertEqual(len(errors), 1)
        self.assertIn("skills/x/SKILL.md", errors[0])
        self.assertIn("G0, G1, G2", errors[0])

    def test_prior_work_is_allowed_before_gates(self):
        (self.dir / "intake" / "prior-work" / "old").mkdir(parents=True)
        (self.dir / "intake" / "prior-work" / "old" / "SKILL.md").write_text("skill")
        self.assertEqual(self.errors(), [])

    def test_build_after_g2_passes(self):
        self.confirm_problem()
        self.add_eval()
        self.sign("G0", "G1", "G2")
        (self.dir / "agents" / "a.md").write_text("agent")
        self.assertEqual(self.errors(), [])

    def test_out_of_order_fails(self):
        self.sign("G1")
        self.assertIn("G1 is signed but G0 is not", self.errors())

    def test_g0_needs_confirmed_problem(self):
        self.sign("G0")
        self.assertTrue(any("Status: CONFIRMED" in e for e in self.errors()))

    def test_g2_needs_an_eval(self):
        self.confirm_problem()
        self.sign("G0", "G1", "G2")
        self.assertTrue(any("evals/ has no case" in e for e in self.errors()))

    def test_partial_signature_fails(self):
        self.sign("G0", check="")
        self.assertTrue(any("partly signed" in e for e in self.errors()))

    def test_short_check_fails(self):
        self.confirm_problem()
        self.sign("G0", check="ok")
        self.assertTrue(any("too short" in e for e in self.errors()))

    def test_bad_date_fails(self):
        self.confirm_problem()
        self.sign("G0", signed_on="yesterday")
        self.assertTrue(any("YYYY-MM-DD" in e for e in self.errors()))


if __name__ == "__main__":
    unittest.main()
