# evals/

Acceptance tests, written at G2 from `PROBLEM.md`, before anything is built.
At least one case per success measure.

Format (`claude plugin eval`):

```
evals/<case-name>/prompt.md            frontmatter (max_turns, allowed_tools, tags) + the task
evals/<case-name>/graders/criteria.md  frontmatter (type: llm, weight) + pass and fail rules
```

Write each grader so a failing output is easy to name: list what must be
present, and end with a "Fail if" line for the one thing that must never
happen. `intake/prior-work/research-design-agents-v2/evals/` has four cases from the prior work.

Run every case with and without the build (the default), at least two runs
per case, and record the results in `EVALS.md` with the date and cost:

```powershell
claude plugin eval . --runs 2 --no-publish --max-cost-usd 6
```
