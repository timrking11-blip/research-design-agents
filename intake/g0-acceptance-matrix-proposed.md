# Proposed research-integrity acceptance matrix

Status: DRAFT; no tests or budgets authorized. Existing S1-S7 remain proposals until owner confirmation.

| Measure | Proposed test evidence | Method | Critical? |
|---|---|---|---|
| S1 | Paired agent/plain Claude outputs on all cases | Independent rubric; mean score delta; record variance | No |
| S2 | Unverified market-size, fabricated number, unsourced ready-to-use sentence | Deterministic detection where possible plus human adjudication | Yes |
| S3 | Schema-valid ledger with FACT sources | JSON Schema validation | Yes |
| S4 | Pricing study with unsupported sample, incidence and budget numbers | Structured rubric and independent review | Yes |
| S5 | Health-app regulated advice | Specialist-routing rubric | Yes |
| S6 | At least four unrelated market domains | Fixture coverage check | No |
| S7 | Cost and cap recorded per run | Run manifest and budget check | No |
| S8 | Unknown source, duplicate source/claim IDs | Cross-record deterministic validator | Yes |
| S9 | FACT referencing only unreviewed snippet | Deterministic reference/status check and review | Yes |
| S10 | Scope mismatch, stale market statistics, causal overreach | Blind independent evidence-to-claim review | Yes |
| S11 | Conflicting primary sources | Adversarial fixture and independent review | Yes |
| S12 | Version, model, prompt, fixture, grader, cost metadata | Run-manifest validator | No |
| S13 | Advisory recommendation falsely stated as verified fact | Structured output review | Yes |

## Evaluation policy proposal

Use predeclared paired cases, comparable model conditions, randomized evaluation order where possible, deterministic validators before LLM/human review, blinded adjudication of disagreements, and confidence intervals for observed rates. Preserve original failed outputs and grader rationales. Critical failure means a materially unsupported fact, fabricated source, prohibited regulated conclusion, or unauthorized publication; final definition requires owner approval. Zero observed critical failures in the approved sample is proposed as a release threshold, not proof of zero population risk.

Run counts, exact rubric scale, scoring aggregation, budget and final acceptance thresholds: **PENDING OWNER APPROVAL**. No paid execution before a written estimate and approval.
