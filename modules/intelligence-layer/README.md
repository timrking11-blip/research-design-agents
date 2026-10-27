# Intelligence-layer module

For builds whose outputs may feed the AI-native intelligence layer. The
layer's target object model is ADR-012 in `Claude-Artifacts`
(`architecture/adr/ADR-012-ai-native-intelligence-core.md`). On 14 Oct 2026
that ADR is **Proposed**, not accepted, and says nothing in it authorizes a
store, a tool, outreach, enrichment spend or an autonomous write. Notion's
"09 — Architecture Roadmap" calls the layer planning input, not an approved
specification. Recheck both before relying on this page.

## What a build using this module does

- It produces typed outputs another system can ingest, and writes to no
  system of record itself. Add the target system to `never_writes` in
  `architecture/system-of-record.yaml`.
- It keeps evidence and assertions apart: sources, claims, hypotheses and
  contradictions are separate records, never one blended paragraph.
- Moving its outputs into the CRM or any system of record is the owner's
  decision, made in the repository that owns that system and under its rules
  (run-log line; hold over 5 records).

## Mapping to the ADR-012 objects

Shown with the research module's ledger (`intake/prior-work/research-design-agents-v2/schemas/ledger.schema.json`):

| Build output | ADR-012 object |
|---|---|
| Source records (excerpt, locator, accessed date) | Evidence, Observation |
| Claims with status FACT | Claim |
| Claims with status INFERENCE or ASSUMPTION | Hypothesis |
| Disagreeing sources; claim `conflicts` | Contradiction |
| Claim `source_ids`, `superseded_by` | ProvenanceEdge |
| Recommendations | Recommendation |
| "Decisions that need a human owner" | Decision (made by a person) |

## Invariant candidates

Add to `architecture/invariants.yaml` as `candidate` rules (ADR-012 is
Proposed, so none is normative):

- Every FACT claim carries at least one source id.
- No output is written to a system of record by the build itself.
- A superseded claim keeps its record and names its successor.
