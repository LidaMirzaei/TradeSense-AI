# 0001. Unified M01–M08 milestone numbering

- Status: Accepted
- Date: 2026-10-19
- Responsibilities: R1, R6
- Milestones: M01–M08

## Context

Two milestone schemes existed side by side:

- `README.md` and `docs/learning-path.md` listed eight milestones numbered 01–08, focused on the TLOB forecasting pipeline.
- `docs/rbc-responsibility-map.md` listed seven stages, M01–M07, which added a commercial-requirements and pricing-baseline stage, the Avellaneda–Stoikov quoting work, and a user-feedback stage, but had no separate predictive-evaluation stage.

The same number referred to different work depending on the document (for example, "05" meant TLOB experiments in one and the reservation-price model in the other). That makes reviews, commit messages, and lessons ambiguous.

## Decision

Use one scheme, M01–M08, in every project document. Each scope item from both earlier schemes maps to exactly one new milestone:

| New | Scope | Previous README / learning path | Previous responsibility map |
| --- | --- | --- | --- |
| M01 | Top-of-book features and tests | 01 | M01 |
| M02 | Commercial requirements, KPIs, quote spec, pricing baseline | — | M02 |
| M03 | Data provenance, parsing, labels, chronological splits, scale benchmarking | 02, 03 | M03 |
| M04 | Majority/logistic baselines and TLOB training | 04, 05 | M04 |
| M05 | Predictive evaluation: macro-F1, calibration, failure cases, latency | 06 | — |
| M06 | Avellaneda–Stoikov reservation price, fill simulator, spread-aware simulation, hybrid integration | 07 | M05 |
| M07 | API, Docker, CI, monitoring, reliability | 08 | M06 |
| M08 | Dashboard, user-feedback experiments, documentation | — | M07 |

No scope item was added or removed. Only the grouping and numbering changed.

## Alternatives considered

- **Keep the README's 01–08 and fold the map's extra stages into them.** Rejected: the commercial-framing (R1) and user-feedback (R5) work would end up as sub-items of unrelated milestones and would be easy to drop.
- **Extend to M01–M10 with no merging.** Rejected: the project owner asked for M01–M08, and the merged pairs (audit + splits, baselines + TLOB) are naturally sequential parts of the same work.

## Consequences

- Every document, PR, lesson, and ADR refers to milestones only as M01–M08.
- M03 and M04 are broader than the old milestones 02–05 were. Their lessons may need sub-steps, but sub-steps keep the parent milestone ID.
- Responsibility IDs for the new M05 (R2, R3) were assigned during this change, because the earlier map had no matching stage. The architect should confirm them.
- The interview-defense questions for M02 and M08 in `docs/learning-path.md` are new, because those milestones previously had no learning-path row.
