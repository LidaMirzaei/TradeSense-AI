# TradeSense AI

**Research-driven limit order book forecasting and simulated execution-cost analysis.**

## Research problem
Can a model predict the near-term direction of mid-price changes from limit order book (LOB) observations? More importantly, can those signals support better *simulated* execution decisions once bid-ask spread and other assumed costs are considered?

This is an educational research prototype, not a live trading system or evidence of trading profitability.

## Research reference
- Berti and Kasneci (2025), *TLOB: A Novel Transformer Model with Dual Attention for Stock Price Trend Prediction with Limit Order Book Data*: https://arxiv.org/abs/2502.15757
- Authors' code: https://github.com/LeonardoBerti00/TLOB
- FI-2010 benchmark paper: https://doi.org/10.1002/for.2543

## Project milestones
Milestones use the IDs M01–M08 across all project documents; see [docs/learning-path.md](docs/learning-path.md) and [docs/rbc-responsibility-map.md](docs/rbc-responsibility-map.md).

- **M01** Implement and test basic top-of-book features.
- **M02** Frame commercial requirements and KPIs; specify quotes and a fixed-spread pricing baseline.
- **M03** Audit FI-2010 provenance, schema, access, and licensing; establish time-aware splits and leakage prevention.
- **M04** Train majority-class and logistic regression baselines; implement TLOB under identical evaluation rules.
- **M05** Evaluate macro-F1, calibration, failure cases, and latency.
- **M06** Assess spread-aware **simulated** decisions with an Avellaneda–Stoikov quote engine, explicitly stating assumptions.
- **M07** Add FastAPI, tests, CI/CD, Docker, and monitoring.
- **M08** Add a user-facing dashboard, feedback experiments, and documentation.

## Status
**M01: Initial scaffold.** No models have been trained and no empirical results have been measured or claimed.

## Run the M01 lesson
Python 3.10+ is enough. No external libraries required.

```bash
git clone https://github.com/LidaMirzaei/TradeSense-AI.git
cd TradeSense-AI
python -m unittest discover -s tests -v
python -m src.market_features
```

## Repository layout
- `src/market_features.py`: first order-book calculations
- `tests/test_market_features.py`: unit tests
- `docs/learning-path.md`: milestone-by-milestone (M01–M08) exercises and interview checks
- `docs/data-and-evaluation.md`: dataset provenance and experiment protocol
- `docs/adr/`: Architecture Decision Records

Raw data, models and results will only be included after access, licensing and verification. Referenced research remains attributed; a license for independently written code can be selected before wider reuse.

## RBC role alignment and pricing extension
See [the six-responsibility map and linked TLOB + Avellaneda–Stoikov design](docs/rbc-responsibility-map.md). The pricing module is planned, not yet implemented.
