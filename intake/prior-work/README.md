# intake/prior-work/

Work written before this repository existed: drafts, agents, skills, schemas,
documents from another repository or a chat. It waits here. It is not part of
the build and CI does not treat it as built.

## Bringing something in

1. Copy it into `intake/prior-work/<name>/` unchanged, with a `SOURCE.md`
   giving where it came from (repository, path, commit or date) and any test
   results it already has.
2. List it under "Prior work" in `PROBLEM.md`.

## Promoting it into the build (after G2)

For each file:

1. Name the `PROBLEM.md` line it serves. A file that serves none stays here
   or is deleted.
2. Run the build's evals with it. Record the result in `EVALS.md`.
3. Move it into `agents/`, `skills/`, `schemas/` or `src/` in a pull request
   that says which line it serves and what the evals showed.

Prior work never decides the problem or the architecture; it is checked
against them.
