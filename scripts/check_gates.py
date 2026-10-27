"""Fail when work runs ahead of the owner's gates.

Reads gates.yaml and checks:
  - each gate is either unsigned or fully signed (signed_by, a YYYY-MM-DD
    signed_on, and a check of at least 12 characters);
  - gates are signed in order;
  - G0 signed means PROBLEM.md says "Status: CONFIRMED";
  - G2 signed means at least one eval case (evals/<case>/prompt.md);
  - nothing besides README.md sits in a build path until G0-G2 are signed.

It checks order and completeness only. It cannot tell who edited gates.yaml;
CODEOWNERS routes that file to the owner, and nothing here signs a gate.

Usage: python scripts/check_gates.py [ROOT]
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

MIN_CHECK_LEN = 12
BUILD_GATES = ("G0", "G1", "G2")
SIGN_FIELDS = ("signed_by", "signed_on", "check")


def _signed(gate: dict) -> tuple[bool, str | None]:
    """(signed, problem): problem names a partial or malformed sign-off."""
    values = {f: str(gate.get(f) or "").strip() for f in SIGN_FIELDS}
    filled = [f for f, v in values.items() if v]
    if not filled:
        return False, None
    if len(filled) < len(SIGN_FIELDS):
        missing = ", ".join(f for f in SIGN_FIELDS if f not in filled)
        return False, f"{gate['id']} is partly signed: missing {missing}"
    try:
        date.fromisoformat(values["signed_on"])
    except ValueError:
        return False, f"{gate['id']} signed_on is not a YYYY-MM-DD date: {values['signed_on']!r}"
    if len(values["check"]) < MIN_CHECK_LEN:
        return False, (f"{gate['id']} check is too short to say what was checked "
                       f"(at least {MIN_CHECK_LEN} characters)")
    return True, None


def _built_files(root: Path, build_paths: list[str]) -> list[str]:
    found = []
    for name in build_paths:
        base = root / name
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if path.is_file() and path.relative_to(base).as_posix() != "README.md":
                found.append(path.relative_to(root).as_posix())
    return found


def check(root: Path) -> tuple[list[str], list[str]]:
    """Return (errors, signed gate ids)."""
    gates_file = root / "gates.yaml"
    if not gates_file.is_file():
        return ["gates.yaml is missing"], []
    config = yaml.safe_load(gates_file.read_text(encoding="utf-8")) or {}
    gates = config.get("gates") or []
    build_paths = config.get("build_paths") or []
    ids = [g.get("id") for g in gates]
    if ids[:3] != list(BUILD_GATES):
        return [f"gates.yaml must list G0, G1, G2 first; found {ids}"], []

    errors: list[str] = []
    signed: list[str] = []
    for i, gate in enumerate(gates):
        ok, problem = _signed(gate)
        if problem:
            errors.append(problem)
        if ok:
            unsigned_before = [g["id"] for g in gates[:i] if g["id"] not in signed]
            if unsigned_before:
                errors.append(f"{gate['id']} is signed but {', '.join(unsigned_before)} is not")
            signed.append(gate["id"])

    if "G0" in signed:
        problem_md = root / "PROBLEM.md"
        text = problem_md.read_text(encoding="utf-8") if problem_md.is_file() else ""
        if not re.search(r"^Status:\s*CONFIRMED\s*$", text, re.MULTILINE):
            errors.append('G0 is signed but PROBLEM.md does not say "Status: CONFIRMED"')

    if "G2" in signed and not list((root / "evals").glob("*/prompt.md")):
        errors.append("G2 is signed but evals/ has no case (evals/<case>/prompt.md)")

    built = _built_files(root, build_paths)
    pending = [g for g in BUILD_GATES if g not in signed]
    if built and pending:
        listed = "\n    ".join(built)
        errors.append(f"build paths hold files while {', '.join(pending)} unsigned:\n    {listed}\n"
                      "  Move them to intake/prior-work/ until the gates are signed.")
    return errors, signed


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errors, signed = check(root)
    if errors:
        for e in errors:
            print(f"gates: {e}")
        return 1
    print(f"gates: ok (signed: {', '.join(signed) or 'none'})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
