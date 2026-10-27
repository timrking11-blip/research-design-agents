# Architecture

This folder is the build's architecture authority. Start here.

| File | Holds |
|---|---|
| `system-of-record.yaml` | The one definition of who owns each object and who may write it |
| `adr/` | Decisions, one per file, Proposed or Accepted |
| `gaps/README.md` | Where decision, code and runtime disagree, or evidence cannot settle a question |
| `invariants.yaml` | Rules the build must keep, with the probes that test them |

## Rules

- **One owner per object.** Ownership is defined only in
  `system-of-record.yaml`. Other files link to it; they never restate it.
- **Three tiers, never mixed.** `current` (true today, with evidence),
  `accepted_target` (accepted by the owner, not yet true), `proposed` (in a
  Proposed ADR; no write authority).
- **Decisions are the owner's.** An ADR filed here, a Notion page or a merge
  never accepts a decision. Only the owner's Accepted status does.
- **Accepted text is never edited.** Add a dated annotation or a new ADR that
  supersedes it.
- **Candidate rules are reported, normative rules are held.** An invariant is
  `normative` only when its ADR is Accepted; until then it is a `candidate`.
- **Existing hard controls never regress.** A control that works today stays
  a must-not-regress check, even under a candidate rule.

## G1 asks for

1. `system-of-record.yaml` filled for every object the build touches.
2. A `never_writes` list: systems of record the build must not write to.
3. `adr/ADR-001-<slug>.md`, Accepted by the owner.
4. A gap for every question the evidence cannot settle.
