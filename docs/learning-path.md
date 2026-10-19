# Learning path — one verified milestone at a time

| Milestone | Deliverable | Interview defense |
|---|---|---|
| 01 | Best bid/ask, spread, midpoint, queue imbalance; tests | What information is missing from a single snapshot? |
| 02 | Dataset audit and reproducible parsing | How do you validate source data? |
| 03 | Label definition and chronological splits | How do you prevent future-data leakage? |
| 04 | Majority baseline and logistic regression | Why is a simple baseline essential? |
| 05 | TLOB-style PyTorch experiments | What do temporal and feature attention capture? |
| 06 | Error analysis, macro-F1, calibration | How stable is performance across market conditions? |
| 07 | Spread-aware execution *simulation* | Why doesn't F1 establish positive P&L? |
| 08 | API, Docker, CI, monitoring | How would you own the system in production? |

## Lesson 01: Your exercise
Input: best bid 100.00, best ask 100.02, displayed bid size 800, displayed ask size 500.

- Compute spread = ask - bid.
- Compute midpoint = (bid + ask) / 2.
- Compute queue imbalance = (bid_size - ask_size) / (bid_size + ask_size).
- Run the existing code and tests.
- Add one new edge-case test yourself.
- Explain why positive queue imbalance is **not** proof the price will rise.

**Interview question:** Name at least three reasons a classifier with strong F1 might still fail as a trading decision system.

Don't proceed to model training until this milestone is understood.
