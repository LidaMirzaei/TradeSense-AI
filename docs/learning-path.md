# Learning path — one verified milestone at a time

| Milestone | Deliverable | Interview defense |
|---|---|---|
| M01 | Best bid/ask, spread, midpoint, queue imbalance; tests | What information is missing from a single snapshot? |
| M02 | Commercial requirements, KPIs, quote specification and fixed-spread pricing baseline | Which measurable KPI would tell a desk that automated quotes are better? |
| M03 | Dataset audit, reproducible parsing, label definition, chronological splits, scale benchmarking | How do you validate source data? How do you prevent future-data leakage? |
| M04 | Majority baseline, logistic regression and TLOB-style PyTorch experiments | Why is a simple baseline essential? What do temporal and feature attention capture? |
| M05 | Error analysis, macro-F1, calibration, failure cases, latency | How stable is performance across market conditions? |
| M06 | Avellaneda–Stoikov reservation price, fill simulator, spread-aware execution *simulation* and forecast-adjusted quoting | Why doesn't F1 establish positive P&L? |
| M07 | API, Docker, CI, monitoring, operational reliability | How would you own the system in production? |
| M08 | User-facing dashboard, feedback experiments and documentation | How do you show a change was driven by real user feedback? |

## M01 lesson: Your exercise
Input: best bid 100.00, best ask 100.02, displayed bid size 800, displayed ask size 500.

- Compute spread = ask - bid.
- Compute midpoint = (bid + ask) / 2.
- Compute queue imbalance = (bid_size - ask_size) / (bid_size + ask_size).
- Run the existing code and tests.
- Add one new edge-case test yourself.
- Explain why positive queue imbalance is **not** proof the price will rise.

**Interview question:** Name at least three reasons a classifier with strong F1 might still fail as a trading decision system.

Don't proceed to model training until this milestone is understood.
