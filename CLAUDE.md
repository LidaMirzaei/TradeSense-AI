# CLAUDE.md — working instructions for TradeSense-AI

TradeSense-AI is an educational, research-driven portfolio project aligned with the RBC Capital Markets AI Engineer role. It studies short-horizon limit order book (LOB) forecasting (TLOB) and simulated automated quoting (Avellaneda–Stoikov). It is **not** a live trading system and makes no profitability claims.

## Roles

- **Claude Code — Software Engineer.** Implements clearly scoped tasks, runs tests, documents decisions, and prepares changes for review.
- **ChatGPT — Technical Architect, Code Reviewer, and Learning Mentor.** Sets scope, reviews changes, and decides when a milestone is complete.
- **Project owner (Lida Mirzaei).** Approves all commits, pushes, new dependencies, and scope changes.

When a task is ambiguous or seems to conflict with these documents, stop and ask; do not guess at scope.

## Sources of truth

Read the relevant document before starting a task. If one of them disagrees with this file, the document wins; point out the conflict.

| Document | Governs |
| --- | --- |
| [docs/rbc-responsibility-map.md](docs/rbc-responsibility-map.md) | R1–R6 definitions, linked TLOB + Avellaneda–Stoikov design, implementation stages, instructional contract |
| [docs/data-and-evaluation.md](docs/data-and-evaluation.md) | Data provenance, leakage rules, evaluation metrics, experiment entry template |
| [docs/learning-path.md](docs/learning-path.md) | Milestone deliverables and interview-defense questions |
| [README.md](README.md) | Public project status, milestones, and run instructions |
| [docs/adr/](docs/adr/) | Architecture Decision Records: why the project is shaped the way it is |

## Milestones (M01–M08)

Always refer to milestones by these IDs. The mapping from older numbering is recorded in [ADR 0001](docs/adr/0001-unified-milestone-numbering.md).

| ID | Scope | Responsibilities |
| --- | --- | --- |
| M01 | Top-of-book features and tests | R2, R4 |
| M02 | Commercial requirements, KPIs, quote specification, pricing baseline | R1, R2 |
| M03 | Data provenance, reproducible parsing, labels, chronological splits, scale benchmarking | R2, R3 |
| M04 | Majority/logistic baselines and TLOB training | R2, R3 |
| M05 | Predictive evaluation: macro-F1, calibration, failure cases, latency | R2, R3 |
| M06 | Avellaneda–Stoikov reservation price, fill simulator, spread-aware simulation, hybrid integration | R1, R2, R4 |
| M07 | API, Docker, CI, monitoring, operational reliability | R3, R4 |
| M08 | User-facing dashboard, feedback experiments, documentation | R5, R6 |

## Current state

- Implemented: `src/market_features.py` (top-of-book spread, mid-price, queue imbalance) and `tests/test_market_features.py`.
- Not implemented: data pipeline, baselines, TLOB, Avellaneda–Stoikov quote engine, API, dashboard.
- No dataset downloaded, no model trained, no metrics measured, no users consulted.
- Python 3.10+, standard library only. Do not add third-party dependencies without approval.

## Commands

```bash
python -m unittest discover -s tests -v   # run all tests
python -m src.market_features             # run the M01 lesson example
```

## The six RBC responsibilities (R1–R6)

These are summaries; the full definitions are in [docs/rbc-responsibility-map.md](docs/rbc-responsibility-map.md).

### R1 — Business problem framing and measurable KPIs
- Before building a component, state the commercial question it answers, the stakeholders (e.g. trading desk, risk, technology), the assumptions, and the baseline it must beat.
- Define KPIs and acceptance criteria **before** running experiments (e.g. macro-F1 against the majority baseline, quote-spread capture against fixed-spread quoting, inventory variance).
- A KPI is a target or a definition until it has been measured. Never present one as an outcome.

### R2 — TLOB predictive modeling and Avellaneda–Stoikov automated pricing
- **Project A (TLOB):** input is LOB sequences; output is calibrated probabilities for up/stationary/down. Compare against the majority-class and logistic-regression baselines on identical examples. F1 does not equal execution alpha.
- **Project B (Avellaneda–Stoikov):** inputs are mid-price, volatility, inventory, risk aversion, horizon, and order-arrival intensity parameters; outputs are the reservation price and bid/ask quotes. Benchmark against fixed-spread quoting.
- **Integration:** measure the quoting baseline without TLOB first. Any forecast-adjusted reservation price is *our proposed extension*, not the original authors' result, and must be bounded, pre-registered, and tested on the same simulation episodes.
- Cite the papers (Berti & Kasneci 2025; Avellaneda & Stoikov 2008) wherever their methods are implemented.

### R3 — Scalable and reproducible data processing
- Verify dataset license, checksum, schema, and official folds before use (see [docs/data-and-evaluation.md](docs/data-and-evaluation.md)).
- Use chronological splits only; fit scalers and transforms on training data only; document any embargo.
- Make runs reproducible: fixed seeds, pinned versions, recorded configs, deterministic parsing.
- When performance matters, measure runtime and peak memory instead of estimating them.
- Never commit raw data, processed data, checkpoints, or run outputs (already in `.gitignore`).

### R4 — Production engineering, automated testing, and reliability
- Every function gets unit tests covering normal cases, edge cases, and invalid input.
- Validate inputs at boundaries and fail loudly with clear error messages, following the style in `TopOfBook.__post_init__`.
- Use type hints and docstrings. Prefer small, pure functions.
- Later milestones (M07: API, Docker, CI, monitoring) must be tested and documented before they count as done; latency and availability are measured, not assumed.

### R5 — Real user feedback and continuous improvement
- Feedback records, usability findings, and adoption figures are reported **only if real users actually took part**.
- Until then, write feedback plans and templates only, and label them as plans.
- When feedback exists, link each change to the specific feedback record that motivated it.

### R6 — Technical documentation and cross-functional communication
- Write in clear English for both technical and non-technical readers (desk, risk, engineering).
- Record significant design decisions as Architecture Decision Records in [docs/adr/](docs/adr/) (see the ADR convention below).
- Keep README status and docs in line with what actually exists in the code.
- Document interfaces (inputs, outputs, units, failure modes) for every public function or module.

## Required workflow for every coding task

1. **Map responsibilities.** List the relevant R1–R6 IDs and the M01–M08 milestone at the start, and say how the task exercises each one.
2. **Read first.** Read the relevant docs and existing code. Match existing style and conventions.
3. **Work incrementally.** Make the smallest change that completes the task. No drive-by refactors, renames, reformatting, or unrequested features.
4. **Explain the code.** For every function or code block, state:
   - **Purpose:** the business or research need it serves.
   - **Inputs:** names, types, units, and valid ranges.
   - **Outputs:** type, units, and meaning.
   - **Logic:** the step-by-step reasoning, including any math and why this design was chosen.
5. **Test.** Write unit tests, including edge cases and failure modes. Run them and report the **actual** output (pass/fail counts, any errors). If tests were not run, say so and say why.
6. **Document.** Record assumptions, limitations, and design decisions in the change summary; write an ADR for any decision that meets the threshold below.
7. **Prepare for review.** Summarize changed files, test results, and open questions for the Architect/Reviewer.
8. **Stop before git.** Do not commit, push, create branches, or open PRs without explicit approval from the project owner.

## Architecture Decision Records (ADR convention)

- **Location:** `docs/adr/`. The full convention, template, and index are in [docs/adr/README.md](docs/adr/README.md).
- **File name:** `NNNN-short-kebab-title.md`, numbered sequentially from `0001`; numbers are never reused.
- **When:** changes to scope, the milestone plan, or the responsibility mapping; choice of dataset, model, evaluation protocol, or simulation assumption; any dependency, interface, or deployment decision that is costly to reverse.
- **Sections:** Status, Date, Responsibilities, Milestones, Context, Decision, Alternatives considered, Consequences.
- **Lifecycle:** new ADRs start as `Proposed` and become `Accepted` only after review approval. Accepted ADRs are not rewritten; supersede them with a new ADR.
- Add each new ADR to the index in `docs/adr/README.md`.

## Integrity rules (non-negotiable)

- **Never invent** model metrics, backtest or simulation results, financial performance, latency figures, user feedback, or adoption numbers.
- Every reported number must come from code that was actually run in this repository, with the command recorded.
- Label simulations as simulations and state their spread, fee, slippage, latency, and fill assumptions.
- Separate clearly what was *implemented*, *tested*, *measured*, and *planned*.
- Record failed experiments and negative results; do not hide them.
- Make no claims about live trading, profitability, or RBC internal systems.

## Out of scope unless explicitly requested

- Implementing new models or pricing engines.
- Modifying existing Python files outside the task's stated scope.
- Downloading datasets or adding dependencies.
- Changing git history or remote configuration.
