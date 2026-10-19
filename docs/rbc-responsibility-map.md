# RBC AI Engineer responsibility map — project contract

This document is the permanent source of truth for scope and teaching. Every future PR, module and lesson should state applicable responsibility IDs (R1–R6), how they are exercised, how they will be verified, and the limits of the evidence.

| ID | Job responsibility | Implementation | Evidence to collect |
| --- | --- | --- | --- |
| R1 | Frame ambiguous commercial questions as evaluable applied-AI problems | Problem statement, assumptions, stakeholders, baseline and measurable KPIs | Requirements, use cases, acceptance criteria |
| R2 | Predictive analytics for electronic trading and automated price setting | TLOB direction classifier + inventory-aware Avellaneda–Stoikov quote engine + *experimental* signal adjustment | Predictive metrics, quote quality, cost/risk benchmarks |
| R3 | Computation at scale | Time-series processing, efficient feature extraction, profiling and load tests | Runtime, peak memory, reproducibility, failure handling |
| R4 | End-to-end AI delivery and adoption | Versioned model, API, container, CI, monitoring and documented deployment | Tests, latency, availability, reproducible operations |
| R5 | Learn from user feedback | Desk-oriented dashboard, usability evaluation, feedback records and changes | User study results *only if users actually participate* |
| R6 | Communicate across teams | Clear English docs, ADRs, interfaces, diagrams and demo | Reviews, decision logs, onboarding documentation |

## Linked research modules

**Project A: TLOB-based forecasting**
- Input: limit order book sequences.
- Output: calibrated short-horizon class probabilities (up, stationary, down).
- Research: Berti & Kasneci (2025), https://arxiv.org/abs/2502.15757
- Caution: F1 != execution alpha or realized profitability.

**Project B: Automated market-making quotes**
- Baseline: Avellaneda & Stoikov, *High-frequency trading in a limit order book* (Quantitative Finance, 2008). https://math.nyu.edu/inmemoriam/avellaneda/HighFrequencyTrading.pdf
- Inputs: mid-price, volatility, inventory, risk aversion, horizon, execution intensity parameters.
- Outputs: simulated reservation price and bid/ask quotes.
- Validation: compare with fixed-spread quotes; quantify inventory exposure and simulation P&L.
- Caveat: modeled fills and prices do not establish live profitability; calibration needs event-level market data.

**Integration experiment**
- First measure the quoting baseline *without* TLOB.
- Convert calibrated TLOB probabilities into a conditional expected mid-price change only after separately estimating conditional magnitudes on training data.
- Hypothesis: adding a bounded forecast term to the reservation price may improve a pre-specified risk-adjusted metric.
- Test: fixed quoting vs Avellaneda–Stoikov vs forecast-adjusted quoting, on the same simulation episodes, with costs and leakage controls.
- A forecast-conditioned variant is our proposed extension, NOT the original authors' result. Limit dependence on FI-2010: it does not establish actual fills or market-making P&L.

## Instructional contract for every code block

1. Label relevant R1–R6 IDs.
2. Explain the business need, inputs and outputs.
3. Walk through code statements and Python syntax.
4. Explain math/algorithms and the reason for the design.
5. Demonstrate a test, including failure modes and edge cases.
6. Ask the learner to explain or modify the block before progressing.
7. Commit only verified outcomes; never fabricate metrics, users, or experiments.

## Implementation stages

- M01 top-of-book features and tests (R2, R4): initial code created, execution verification pending.
- M02 commercial requirements, quote specification and pricing baseline (R1, R2).
- M03 data provenance, time-aware pipelines and scale benchmarking (R2, R3).
- M04 model baselines and TLOB training (R2, R3).
- M05 reservation-price model, fill simulator and hybrid integration (R1, R2, R4).
- M06 API, operational reliability and deployment (R3, R4).
- M07 user-facing dashboard, feedback experiments and documentation (R5, R6).

Status: design only for new pricing components. No trading or profitability claims.
