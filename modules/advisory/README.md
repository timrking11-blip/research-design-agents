# Advisory module

Rules for builds that serve client or prospect work: research on a company,
proposals, notes to a founder, records in a CRM. Generalized from the rules
the owner set in Claude-Artifacts after things went wrong. Copy the sections
the build needs into its `CLAUDE.md` and `architecture/invariants.yaml`.

## The intake form is the specification

- **Domain lock.** Research only the company at the exact domain on the
  intake form. A similarly named company at another domain is a different
  company, even if a search result says otherwise. List lookalikes under Gaps
  and use nothing from them.
- **Empty means empty.** When the intake domain yields nothing, the output
  says "not found". Never fill the gap from a lookalike or a guess.
- **Credit spend.** Paid enrichment runs only when the form allows credit
  spend on that account, only for the intake domain, and only with an
  estimate first.
- **One output per run.** A changed proposal is a new run from the intake
  page, never an edit of one already filed.

## HOLDs clear only after an independent check

- A HOLD, or anything called unconfirmed, is never cleared by a verbal
  "confirmed" alone.
- It clears after one independent check: open the actual domain beside any
  lookalike, pull a second source, or answer "what would confirm this is the
  same company?" and do that check.
- Each HOLD line names its check after "Confirm by:". Record the result where
  the HOLD was raised.

## Run log, and a hold on bulk creation

- Every run that creates or changes records writes one line where the owner
  looks (a run-log collection shown on the CRM page or the morning brief). A
  changelog, CI log or chat reply alone does not count.
- A run that would create more than 5 records holds instead of committing.
  It names the records and the check that confirms them, and applies only
  after the owner confirms that exact count. A different count holds again.
- A confirmation is structured: the check made (at least 12 characters), the
  time, and the confirmed count equal to the count created. A note never
  authorizes a bulk creation.

Run-log line shape:

```json
{
  "run": "name-of-run",
  "at": "YYYY-MM-DDTHH:MM:SSZ",
  "created": 0,
  "updated": 0,
  "status": "applied | held",
  "names": ["records created or held"],
  "check": "the check that confirms them",
  "confirmed_count": null,
  "confirmed_at": null
}
```

## Who an output is addressed to

- The next step and any note go to the person named on the intake form (for
  a small startup, usually its founder).
- The internal review before anything is sent ("Review before sending") is
  for the firm only and is never shown to the prospect.

## Names

- Use the firm's exact registered name from one constant in code, never
  retyped. A wrong name in an append-only record cannot be taken back.
