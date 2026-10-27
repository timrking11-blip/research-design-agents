# Eval results

Each case runs with the plugin and without it (plain Claude Code). Graders are
LLM judges (`claude plugin eval` default: Haiku, three votes). Scores are the
share of runs that passed. These are small samples: treat one or two runs per
case as a signal, not a measurement.

## v2 · 14 Oct 2026 · 2 runs per case · $1.04

| Case | With | Without | Δ |
|---|---|---|---|
| health-app-custom-study | 1.00 | 0.00 | +1.00 |
| pricing-study-design | 1.00 | 1.00 | 0.00 |
| unverified-market-size | 0.50 | 0.00 | +0.50 |
| vague-request-brief | 1.00 | 0.00 | +1.00 |
| **Mean** | | | **+0.63** |

- Both v1 failures moved: pricing-study-design now passes with the plugin;
  unverified-market-size passed in one of two runs with it and none without.
- unverified-market-size still fails half the time with the plugin. Next
  step: read the failing run's output before changing the skill again.
- health-app-custom-study passed without the plugin in v1 and failed without
  it here. Plain Claude's result on that case is unstable, which is why one
  run per case was not enough.

## v1 · 14 Oct 2026 · 1 run per case · $0.48

| Case | With | Without | Δ |
|---|---|---|---|
| health-app-custom-study | 1.00 | 1.00 | 0.00 |
| pricing-study-design | 0.00 | 1.00 | −1.00 |
| unverified-market-size | 0.00 | 0.00 | 0.00 |
| vague-request-brief | 1.00 | 0.00 | +1.00 |
| **Mean** | | | **0.00** |
