# Gates

Each gate is a point where the owner steps in before the next stage of work
starts. Claude prepares what the gate needs and stops; the owner checks it and
signs in `gates.yaml`.

## G0 Problem confirmed

- **Claude prepares:** a draft `PROBLEM.md` from the owner's description, with
  every unknown marked "not known" or `ASSUMPTION`, and the open questions
  listed.
- **Owner checks:** the problem, the decision and the success measures are
  right; nothing in "Out of scope" is needed.
- **Signed when:** `PROBLEM.md` says `Status: CONFIRMED` with the date and the
  owner's name, and G0 carries the check made.
- **Nothing else is written before this**, except files under
  `intake/prior-work/`.

## G1 Boundaries accepted

- **Claude prepares:**
  - `architecture/system-of-record.yaml`: each object the build touches, the
    one store that owns it, and who may write it;
  - the stores the build never writes to;
  - `architecture/adr/ADR-001-*.md` with the first consequential choice;
  - gaps for anything the evidence cannot settle.
- **Owner checks:** the ownership is right, and the boundaries hold the
  build away from systems of record it must not touch.
- **Signed when:** ADR-001 is Accepted by the owner and G1 carries the check.

## G2 Acceptance defined

- **Claude prepares:** eval cases under `evals/<case>/` (`prompt.md` and
  `graders/criteria.md`), at least one per success measure, written from
  `PROBLEM.md` and not from any existing build.
- **Owner checks:** passing these cases would mean the problem is solved.
- **Signed when:** G2 carries the check. Building starts after this.

## G3 Build reviewed

- **Claude prepares:** the build in the build paths, the eval results (with
  and without the build where that applies), and the pull request.
- **Owner checks:** the build does what `PROBLEM.md` says and stays inside the
  boundaries. Claude never merges.
- **Signed when:** the owner has reviewed the results and signs G3.

## G4 Released

- **Claude prepares:** release notes and the final eval results.
- **Owner checks:** results meet the threshold in `PROBLEM.md`.
- **Signed when:** G4 carries the check.

## Changing a signed gate

A change to `PROBLEM.md` after G0 is a new version. It reopens every later
gate: clear their sign-offs in the same pull request and say why in
`PROBLEM.md`'s change table.
