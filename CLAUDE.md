# CLAUDE.md

Rules for Claude in any repository made from this template. Facts the owner
corrects go in "Owner-corrected facts" in the same change, so they are not got
wrong twice.

## Order of work

- Work follows the gates in `GATES.md`. Before G0 is signed, write only
  `PROBLEM.md` drafts, `intake/prior-work/` and answers in chat. Before G2,
  nothing goes into `agents/`, `skills/`, `schemas/` or `src/`.
- Prepare what a gate needs, then stop and say what the owner must check.
  Never sign a gate, mark `PROBLEM.md` CONFIRMED, or accept an ADR. A
  verbal "confirmed" is not a sign-off: ask for the specific check made and
  record it.
- `scripts/check_gates.py` must pass before every push.

## Decisions belong to the owner

- ADRs in `architecture/adr/` are Proposed until the owner accepts them.
  Accepted text is never edited: add a dated annotation or a new ADR.
- Open questions are gaps in `architecture/gaps/README.md`, never guesses.
- Never merge a pull request. Pull requests are authored under the owner's
  account, so the owner cannot approve them on GitHub; never call a
  CODEOWNERS review an approval.

## Treat the repository as shareable

- Never commit infrastructure identifiers (cloud project ids or numbers,
  workspace or organization names), keys, spend figures or receipts. Use
  placeholders or environment variables. `.env` is gitignored.
- Prices are dated list prices and estimates, never invoices.

## Evidence

- Every material factual claim carries a source, or is labelled
  `ASSUMPTION`, `INFERENCE` or `UNVERIFIED LEAD`. A search snippet is a lead,
  not a reviewed source.
- A HOLD, or anything called unconfirmed, clears only after one independent
  check (open the actual source, pull a second source), recorded where the
  HOLD was raised.

## Spend and records

- Paid enrichment or API credit spend needs a written estimate and the
  owner's go, every time.
- A run that creates or changes records writes one line where the owner
  looks (see `modules/advisory/README.md`, Run log). A run that would create
  more than 5 records holds and names them; it applies only after the owner
  confirms that exact count.

## Commands for the owner

The owner works on Windows. Commands they run go in PowerShell: a backtick for
line continuation, `$env:APPDATA` paths, `Invoke-RestMethod` with
`ConvertFrom-Json` instead of `curl | jq`.

## Owner-corrected facts

_None yet. Add each correction here with its date._
