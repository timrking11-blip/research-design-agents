# Runtimes

## Primary: Claude Code

Builds are Claude Code plugins: agents in `agents/`, skills in `skills/`,
evals run with `claude plugin eval`. Skills use only the Agent Skills fields
(`name`, `description`, Markdown body) and name no Claude-only tools, so they
stay portable.

## Candidates

A candidate runtime is not adopted until it passes this check, recorded as an
ADR in the build that wants it:

1. **Gap.** What Claude Code cannot do that the runtime would.
2. **Owner.** Who runs, updates and pays for it.
3. **Boundary.** What it may read and write; that it writes to no system of
   record; that any skills or memory it writes for itself come back as a pull
   request a person reviews.
4. **Cost.** Dated list-price estimates for models and hosting.
5. **Acceptance test.** The build's evals score the same or better on it.

### Hermes Agent (Nous Research)

Candidate, not adopted. What was verified on 14 Oct 2026 and what was not is
in `docs/hermes-runtime.md`. In short: open source (MIT), reads the Agent
Skills standard by its own README, connects to MCP servers; direct Anthropic
model support and a way to turn off its self-written skills were not
confirmed.
