# PROBLEM

Status: DRAFT — G0 PROPOSALS PENDING OWNER APPROVAL
Confirmed on: 
Confirmed by: 
Version: 1 (unconfirmed; proposed amendments below)

This file is the specification. Nothing is built until it is CONFIRMED and G0
is signed in `gates.yaml`. A change after confirmation is a new version with a
change line below; the old text stays.

Drafted by Claude on 27 Oct 2026 from the owner's messages of 14 Oct 2026.
Lines marked `ASSUMPTION` are Claude's reading and need the owner's check.

## Business problem

Market research and research design for advisory work is done ad hoc, in chat,
one project at a time. Earlier agents were tied to one project or to a narrow
subject (economics, news cycles), so each new question started from scratch.
Their findings could not be traced back to sources, and nothing stopped an
unchecked figure from reaching a proposal or memo.

The owner wants robust agents for market research and research design that
work for any product, market or category, and whose every claim can be
checked.

## Decision served

1. **Which study to run** for a research question: method, sample, budget
   drivers and timeline, or whether existing evidence already answers it.
   Owner: Tim King for internal questions; the client's named decision owner
   for a custom study.
2. **Whether a claim is fit to use** in a proposal, memo or deck. Owner: Tim
   King, at "Review before sending".

## Users and affected people

- Tim King (SMI), who runs the agents and signs off their output.
- Clients and prospects, usually small-startup founders, who receive study
  plans and proposals. `ASSUMPTION`
- Survey and interview respondents in any study designed with these agents,
  whose personal data a study may collect.

## Success measures

Thresholds are Claude's proposal. The owner sets the final numbers.

| # | Measure | Proposed threshold |
|---|---|---|
| S1 | The agents do better than plain Claude Code on the eval suite | Mean Δ ≥ +0.50 over ≥ 3 runs per case |
| S2 | No unchecked figure is stated as fact in a ready-to-use sentence | The unverified-figure case passes 3 of 3 runs with the agents |
| S3 | Every FACT claim in a ledger carries a source id | 100% of ledgers produced in evals validate against the schema |
| S4 | Study designs label every number not supplied by the user | The pricing-design case passes 3 of 3 runs |
| S5 | Regulated topics are routed to specialist review, never answered with a compliance conclusion | The health-app case passes 3 of 3 runs |
| S6 | Works across categories | Eval cases cover at least 4 unrelated markets |
| S7 | Cost per eval run is known | Each run's cost recorded in `EVALS.md`; one full run ≤ $6 |

## Out of scope

- Writing to the CRM, Apollo or any other system of record. Outputs are files:
  study plans, instruments and ledger JSON.
- Paid enrichment or data purchases.
- Running fieldwork: recruiting panels, sending surveys, conducting
  interviews. `ASSUMPTION`
- Legal, privacy, clinical or regulatory opinions. The agents raise issues and
  questions only.
- Monitoring economic indicators or news cycles.

## Constraints

- No credit or paid-API spend without a written estimate and the owner's go.
  Eval runs are capped with `--max-cost-usd`.
- No identifiable health information unless the owner confirms the
  environment and handling are approved for it.
- Jurisdictions: not known. Each study states its own in its research brief.
- Runtime: Claude Code plugin. Hermes Agent stays a candidate until its
  adoption check passes (`docs/runtimes.md`).
- Commands for the owner are in PowerShell.

## Prior work

- `intake/prior-work/research-design-agents-v2/`: two agents, four skills, a
  ledger schema and four eval cases (plugin 0.2.0). v2 mean Δ +0.63 at two
  runs per case. Source and history are in its `SOURCE.md`.
- `timrking11-blip/Claude-Artifacts` `drafts/research-design-agents/` holds the
  v1 copy. It is removed there once this file is CONFIRMED.

## Open questions

All block G0:

1. Is the primary user SMI's client advisory work, or general use beyond SMI?
2. Are the success thresholds above right?
3. Is running fieldwork out of scope, as assumed?
4. Should outputs later feed the AI-native intelligence layer? If so, the
   hand-off is decided under ADR-012 (Proposed), in Claude-Artifacts, not
   here.
5. Keep `modules/advisory/` in this repo, or delete it?


## Proposed G0 decisions — NOT APPROVED (2026-11-02)

These are recommendations for owner review, **not** answers, confirmation, or a sign-off. The five open questions above remain blocking.

| Question | Proposed disposition | Approval |
|---|---|---|
| D1 Primary user | SMI client advisory first, with reusable cross-industry research architecture | PENDING OWNER |
| D2 Thresholds | Keep S1 mean improvement >= +0.50 as secondary; add deterministic evidence-integrity checks and independent semantic grading. The final sample size and zero-critical-failure threshold require owner approval and a cost estimate. | PENDING OWNER |
| D3 Fieldwork | Design instruments and methods only; exclude recruitment, survey distribution, and interviewing in v1 | PENDING OWNER |
| D4 Intelligence layer | Permit future optional, reviewed file-based handoff; no integration or downstream writes without a separately accepted ADR | PENDING OWNER |
| D5 Advisory module | Retain as isolated optional policy guidance; do not promote recommendations to verified facts | PENDING OWNER |

### Proposed additional success measures (not yet normative)

| ID | Measure | Proposed acceptance / evaluation method |
|---|---|---|
| S8 | Referential integrity | 100% of evaluated ledgers have unique source/claim IDs and all cited source IDs resolve; deterministic validation |
| S9 | Reviewed evidence | 0 ready-to-use FACT claims supported solely by unreviewed snippets; deterministic status checks plus semantic review |
| S10 | Evidence fidelity | No critical unsupported, exaggerated, or scope-mismatched factual assertions in independently adjudicated release evals; sample size and graders to be approved at G2 |
| S11 | Conflicting evidence | All seeded material conflicts are disclosed or the output is held for review; adversarial evaluation |
| S12 | Reproducibility | 100% of evaluation runs record input fixture, agent/prompt version, model identifier/settings where available, grader version, result and cost |
| S13 | Advisory separation | 100% of advisory eval outputs distinguish recommendations and assumptions from verified evidence |

A zero-critical-failure sample is a release gate, **not** a guarantee of zero real-world error. Do not silently convert the proposed measures to signed acceptance criteria.

### Proposed evaluation protocol (not authorized to execute)

Preserve the four prior-work cases; add adversarial cases for fabricated citations, duplicate or missing IDs, contradictory primary sources, stale figures, misleading precision, causal overreach, company/domain lookalikes, regulated topics, and assumption-to-fact promotion. Pair agent and baseline runs using comparable inputs, independent grading, and adjudication of critical failures. Specify a larger sample size and cost estimate for owner approval before any paid execution.

### Explicit G0 review required

The owner must personally review the business problem, both decisions served, all success measures and thresholds, all out-of-scope items, and the five proposed dispositions; then provide a genuine description of the check performed. Only a separate authorized change may mark this file CONFIRMED and sign G0 in gates.yaml.

## Changes

| Version | Date | What changed | Why |
|---|---|---|---|
| 1 | 2026-10-27 | Drafted | Repository created; G0 started |
| 1 draft amendment | 2026-11-02 | Added proposed decisions and acceptance criteria | Owner review only; no confirmation |
