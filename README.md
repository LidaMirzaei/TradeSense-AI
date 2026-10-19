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
1. Implement and test basic top-of-book features.
2. Audit FI-2010 provenance, schema, access, and licensing.
3. Establish time-aware splits and leakage prevention.
4. Train majority-class and logistic regression baselines.
5. Implement and compare TLOB with identical evaluation rules.
6. Evaluate macro-F1, calibration, failure cases, and latency.
7. Assess spread-aware **simulated** decisions, explicitly stating assumptions.
8. Add FastAPI, tests, CI/CD, Docker, and monitoring.

## Status
**Milestone 01: Initial scaffold.** No models have been trained and no empirical results have been measured or claimed.

## Run lesson 01
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
- `docs/learning-path.md`: stage-by-stage exercises and interview checks
- `docs/data-and-evaluation.md`: dataset provenance and experiment protocol

Raw data, models and results will only be included after access, licensing and verification. Referenced research remains attributed; a license for independently written code can be selected before wider reuse.

## RBC role alignment and pricing extension
See [the six-responsibility map and linked TLOB + Avellaneda–Stoikov design](docs/rbc-responsibility-map.md). The pricing module is planned, not yet implemented.
