# Data provenance and experimental integrity

## Proposed initial benchmark
FI-2010 (Ntakaris et al., 2018): https://doi.org/10.1002/for.2543
Fairdata record: https://etsin.fairdata.fi/dataset/73eb48d7-4dbc-4a10-a52a-da745b47a649

**Dataset not yet downloaded or verified in this repository.** Verify permitted use, exact archive contents, checksum, features, labels, and official folds before training.

## Evaluation rules
1. Train/validation/test must respect time. Document all dates and any overlap/embargo.
2. Fit scalers and preprocessing transforms on *training data only*.
3. Do not allow future prices, labels, or normalization statistics to leak into past inputs.
4. Compare majority baseline, logistic regression and neural network on identical labeled examples.
5. Report macro-F1, classwise precision/recall, confusion matrix, and calibration; include uncertainty where feasible.
6. Document shift across days/assets, inference latency, and compute cost.
7. Any execution-cost analysis is a **simulation** with explicit spread, fees, slippage, latency, and fill assumptions.
8. Record unsuccessful experiments and limitations. Do not manufacture performance metrics.

## Experiment entry template
- Question and hypothesis:
- Dataset URL, license, checksum:
- Date range, schema, feature definitions:
- Label horizon, split and leakage checks:
- Model and hyperparameters:
- Seed, hardware, duration:
- Evaluation metrics and comparisons:
- Cost/decision assumptions:
- Failure cases and follow-up:
