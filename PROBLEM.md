# PROBLEM

Status: DRAFT
Confirmed on: 
Confirmed by: 
Version: 2 (draft)

This file is the specification. Nothing is built until it is CONFIRMED and G0
is signed in `gates.yaml`. A change after confirmation is a new version with a
change line below; the old text stays.

Version 1 was drafted by Claude on 27 Oct 2026 from the owner's messages of
14 Oct 2026. Version 2 (1 Nov 2026) adds the owner-supplied audit of 1 Nov:
proposed answers to the five open questions, evidence-integrity success
measures, and an acceptance matrix. Every proposed decision below is marked
**PENDING OWNER APPROVAL** and binds nothing until this file is CONFIRMED.
Lines marked `ASSUMPTION` are Claude's reading and need the owner's check.

## Business problem

Market research and research design for advisory work is done ad hoc, in chat,
one project at a time. Earlier agents were tied to one project or to a narrow
subject (economics, news cycles), so each new question started from scratch.
Their findings could not be traced back to sources, and nothing stopped an
unchecked figure from reaching a proposal or memo.

The owner wants an evidence-based research system, not only agents that write
better reports than plain Claude. It must keep verified findings apart from
inference, weigh conflicting sources, preserve where each claim came from, and
support decisions that can be defended.

The order of work inside the system:

> evidence collection → claim verification → synthesis → advisory
> interpretation → human approval

No step may turn its own interpretation into a verified fact by handing it to
the next step.

## Decision served

1. **Which study to run** for a research question: method, sample, budget
   drivers and timeline, or whether existing evidence already answers it.
   Owner: Tim King for internal questions; the client's named decision owner
   for a custom study.
2. **Whether a claim is fit to use** in a proposal, memo or deck. Owner: Tim
   King, at "Review before sending".

## Proposed decisions (PENDING OWNER APPROVAL)

| # | Question | Proposed answer | Why |
|---|---|---|---|
| D1 | Primary user | SMI's client advisory work first; the architecture stays reusable across industries | Concrete cases make evaluation possible without closing off wider use |
| D2 | Success thresholds | Revise: evidence-integrity measures are primary (S1–S6); the comparison with plain Claude is secondary (S9) | A score improvement alone does not show research quality |
| D3 | Fieldwork | Out of scope for v1. The agents may design screeners, surveys and interview guides; they never recruit, contact or interview anyone | Contact with people needs consent handling and a person in the loop |
| D4 | Intelligence layer | A future, optional export of ledger files is allowed; nothing is committed now, and there are no automatic writes downstream | Keeps research evidence independent of downstream systems; any hand-off is decided under ADR-012 in Claude-Artifacts |
| D5 | Advisory module | Keep `modules/advisory/`, isolated and optional. Advisory recommendations are labelled as interpretation, never as research findings | Stops recommendations being read as verified facts |

## Users and affected people

- Tim King (SMI), who runs the agents and signs off their output.
- Clients and prospects, usually small-startup founders, who receive study
  plans and proposals. `ASSUMPTION`
- Survey and interview respondents in any study designed with these agents,
  whose personal data a study may collect.

## Success measures

Thresholds are proposals, PENDING OWNER APPROVAL. "Critical violation" means
any output, in any eval run, where an unreviewed, fabricated or unsupported
figure or source is presented as a verified fact or in ready-to-use prose, or
where a FACT claim fails the deterministic ledger checks (R1–R4 below).

| # | Measure | Proposed threshold | Primary or secondary |
|---|---|---|---|
| S1 | No critical evidence-integrity violations | 0 across all runs of the full suite | Primary |
| S2 | Ledgers pass the deterministic integrity checks (R1–R4) | 100% of ledgers produced in evals | Primary |
| S3 | Material conflicting evidence is disclosed (R6) | Every conflict case passes in every run | Primary |
| S4 | Advisory interpretation is kept apart from findings (R10) | Every run of the cases that test it | Primary |
| S5 | Regulated topics go to specialist review, never to a compliance conclusion | The regulated-topic cases pass in every run | Primary |
| S6 | Every eval run is reproducible (R9) | Each run records agent version, model and settings, inputs, results and cost | Primary |
| S7 | Works across categories | Cases cover at least 4 unrelated markets | Secondary |
| S8 | Independent grading | Graders are deterministic where possible; LLM-judged cases are spot-checked by the owner or a second judge model | Secondary |
| S9 | Better than plain Claude Code | Mean Δ ≥ +0.50 over paired runs | Secondary |

A zero-failure result shows only that failures are rare, not that they cannot
happen: with 0 failures in N runs, the 95% upper bound on the failure rate is
about 3/N (the "rule of three"). The suite should be sized so that bound is
acceptable to the owner (for example, N = 60 runs gives about 5%).

## Acceptance matrix (research integrity)

Each requirement is defined here at G0. Its tests are written at G2, and it is
implemented at G3. "Deterministic" means code can check it on the ledger file;
"semantic" means it needs review by a person or a calibrated judge.

| # | Requirement | Check | Measure |
|---|---|---|---|
| R1 | Every published FACT claim cites at least one source | Deterministic | S2 |
| R2 | Source ids and claim ids are unique | Deterministic | S2 |
| R3 | Every cited source id resolves to a record in the same ledger | Deterministic | S2 |
| R4 | A FACT cannot rest only on sources marked `reviewed: false` (search snippets, unread listings) | Deterministic | S1, S2 |
| R5 | Every claim carries one status: FACT, INFERENCE, ASSUMPTION or UNVERIFIED_LEAD | Deterministic (schema); semantic (is the status right?) | S1 |
| R6 | Material contradictory evidence is disclosed | Deterministic that a `conflicts` entry exists where two sources disagree on a value; semantic for whether a conflict is material | S3 |
| R7 | Source recency, coverage, independence and limits are assessed | Deterministic that the fields are filled; semantic for their quality | S8 |
| R8 | Unsupported numbers never appear in ready-to-use prose | Partly deterministic (numbers in prose matched to FACT claims); semantic for paraphrase | S1 |
| R9 | Each eval run records agent version, model and settings, inputs, results and cost | Deterministic | S6 |
| R10 | Advisory recommendations are labelled and kept apart from findings | Deterministic for the label and section; semantic for leakage | S4 |
| R11 | A claim's verification is done by a step other than the one that wrote it | Semantic, and by design at G1 | S1 |
| R12 | A cited source's scope supports the claim (population, place, period) | Semantic | S1 |

## Out of scope

- Writing to the CRM, Apollo or any other system of record. Outputs are files:
  study plans, instruments and ledger JSON.
- Paid enrichment or data purchases.
- Running fieldwork: recruiting, sending surveys, conducting interviews
  (proposed D3).
- Legal, privacy, clinical or regulatory opinions. The agents raise issues and
  questions only.
- Monitoring economic indicators or news cycles.

## Constraints

- No credit or paid-API spend without a written estimate and the owner's go.
  This includes eval runs; each is capped with `--max-cost-usd`.
- No identifiable health information unless the owner confirms the
  environment and handling are approved for it.
- Jurisdictions: not known. Each study states its own in its research brief.
- Runtime: Claude Code plugin. Hermes Agent stays a candidate until its
  adoption check passes (`docs/runtimes.md`).
- Commands for the owner are in PowerShell.

## Prior work

- `intake/prior-work/research-design-agents-v2/`: two agents, four skills, a
  ledger schema and four eval cases (plugin 0.2.0). Its reported v2 result,
  mean Δ +0.63 at two runs per case, has not been reproduced in this
  repository. The unverified-figure case passed 1 of 2 runs with the agents.
  Source and history are in its `SOURCE.md`.
- What the prior work already provides: the four claim statuses, required
  source fields (issuer, type, access date, excerpt, `reviewed`), and a schema
  rule that a FACT lists at least one source id.
- What it lacks against the matrix: R2–R4 and R6 (the schema cannot check
  references across records), R9 (runs do not record agent version or
  settings), and R11 (one agent writes and labels its own claims).
- `timrking11-blip/Claude-Artifacts` `drafts/research-design-agents/` holds the
  v1 copy. It is removed there once this file is CONFIRMED.

## Open questions

All block G0:

1. Approve, change or reject D1–D5.
2. Approve or change the thresholds in S1–S9, and the suite size N for S1.
3. Is R11 (a separate verification step) required for v1, or a G3 stretch?

## Changes

| Version | Date | What changed | Why |
|---|---|---|---|
| 1 | 2026-10-27 | Drafted | Repository created; G0 started |
| 2 (draft) | 2026-11-01 | Proposed D1–D5; evidence-integrity measures made primary (S1–S6), Claude comparison secondary (S9); acceptance matrix R1–R12; prior-work gaps listed | Owner-supplied audit of 1 Nov 2026 |
