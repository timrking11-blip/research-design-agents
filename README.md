# research-design-agents

Evidence-governed market research and research design agents, not tied to
one project, industry or news cycle. Started from `build-template`.

**Stage: G0.** `PROBLEM.md` is a draft awaiting the owner's confirmation.
Nothing is built yet: the agents written earlier wait in
`intake/prior-work/research-design-agents-v2/`.

| File | What it holds |
|---|---|
| `PROBLEM.md` | The specification (draft) |
| `gates.yaml`, `GATES.md` | The owner's sign-offs, G0 to G4, and what each needs |
| `architecture/` | System of record, ADRs, gaps, invariants (filled at G1) |
| `evals/` | Acceptance tests (written at G2) |
| `intake/prior-work/` | Work written before this repository existed |
| `modules/` | Optional rules: advisory work; the intelligence-layer mapping |
| `docs/` | Runtimes; Hermes Agent as a candidate |

Checks (PowerShell):

```powershell
python -m pip install pyyaml
python scripts/check_gates.py
python -m unittest discover -s tests
```
