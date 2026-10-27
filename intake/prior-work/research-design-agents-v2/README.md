# Research module (v2)

Evidence-governed market research design: two Claude Code agents, four Agent
Skills, a ledger schema and four eval cases. Not tied to one industry,
project or news cycle.

**Status: draft, not proven.** It was first written on 14 Oct 2026 before its
own repository existed (v1, kept in `Claude-Artifacts/drafts/`). In a new
build it enters through `intake/prior-work/` and is promoted only against that
build's confirmed `PROBLEM.md` and evals.

| Path | What it is |
|---|---|
| `agents/primary-research-designer.md` | Designs studies that collect new data |
| `agents/custom-research-designer.md` | Scopes bespoke client studies |
| `skills/research-brief` | Versioned brief before any research |
| `skills/evidence-ledger` | Source register, claim ledger, search log |
| `skills/primary-research-design` | Method, sampling, instruments, analysis plan |
| `skills/custom-study-scoping` | Client problem to study architecture |
| `schemas/ledger.schema.json` | Machine-readable ledger |
| `evals/` | Four cases for `claude plugin eval` |
| `.claude-plugin/plugin.json` | Plugin manifest (0.2.0) |

## v1 to v2

The v1 eval run (one run per case, with and without the plugin) showed no net
gain. Reading the graded outputs gave two causes:

| Case | v1 result | Cause | v2 change |
|---|---|---|---|
| pricing-study-design | Failed with the plugin, passed without | The design stated "the number of eligible firms is in the tens of thousands" with no label | `primary-research-design`: every number not from the user carries a source or `ASSUMPTION`, including figures inside the sample-size arithmetic |
| unverified-market-size | Failed in both arms | Both wrote a ready-to-paste memo line stating the figure, with a placeholder citation | `evidence-ledger`: no ready-to-use sentence states an unreviewed figure; the doubt goes inside the sentence, or no line is written yet. The skill now also triggers on "put this in my memo" |

v2 eval results are in `EVALS.md`.

## Use

Load it for one session (PowerShell):

```powershell
claude --plugin-dir intake\prior-work\research-design-agents-v2
```

Test it:

```powershell
claude plugin validate intake\prior-work\research-design-agents-v2
claude plugin eval intake\prior-work\research-design-agents-v2 --runs 2 --no-publish --max-cost-usd 6
```
