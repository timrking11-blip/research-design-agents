# PROBLEM

Status: DRAFT
Confirmed on: 
Confirmed by: 
Version: 1

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

## Changes

| Version | Date | What changed | Why |
|---|---|---|---|
| 1 | 2026-10-27 | Drafted | Repository created; G0 started |
