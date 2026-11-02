# Conditional G1–G4 backlog — not authorized

## G1 — Boundaries accepted

1. Complete architecture/system-of-record.yaml with one write authority per object and explicit never_writes for CRM, Apollo, intelligence layer, and external records unless separately approved.
2. Propose ADR-001 defining evidence/output ownership, source storage and human approvals; accept only with owner authorization.
3. Define file handoff interface without activating integrations.
4. Record privacy, source rights, retention, and jurisdiction unknowns as gaps.

## G2 — Acceptance defined

1. Create at least one eval fixture per confirmed success measure; preserve four original fixtures and add adversarial fixtures from the matrix.
2. Define deterministic ledger checks: unique IDs, reference resolution, reviewed status, schema validation and provenance completeness.
3. Define semantic source-support checks, independent grader calibration, critical failure adjudication and run manifests.
4. Propose gate-checker improvement enforcing coverage for each measure, rather than any single prompt. Test negative paths.
5. Obtain owner sign-off before any active implementation.

## G3 — Build reviewed

1. Selectively promote prior-work skills and agents, preserving provenance and regression tests.
2. Implement ledger referential integrity, claim review state, conflict disclosures, and publication hold rules.
3. Run approved paired evaluations within approved budget; publish failures and evidence.
4. Require owner review of build and boundary adherence.

## G4 — Released

1. Verify confirmed critical and secondary thresholds; publish reproducible results and limitations.
2. Owner approval, release notes, version tag and rollback guidance.
3. No automatic downstream intelligence ingestion absent separate accepted ADR.

## Explicit exclusions for this draft PR

No agent implementation, no tests executed, no gate signing, no deletion, no merge, no paid API calls.
