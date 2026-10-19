# Architecture Decision Records

This directory holds the project's Architecture Decision Records (ADRs). An ADR captures one significant technical or scope decision, the context behind it, and its consequences, so reviewers and future contributors can see *why* the project is shaped the way it is (R6).

## When to write an ADR

Write one when a decision:
- changes the project scope, milestone plan, or responsibility mapping;
- selects a dataset, model architecture, evaluation protocol, or simulation assumption;
- introduces a dependency, interface, or deployment choice that is costly to reverse.

Small, local implementation choices belong in code comments or the change summary instead.

## Conventions

- File name: `NNNN-short-kebab-title.md`, numbered sequentially from `0001`. Numbers are never reused.
- Status: `Proposed`, `Accepted`, `Superseded by NNNN`, or `Deprecated`.
- Accepted ADRs are not rewritten. To change a decision, write a new ADR that supersedes the old one and update the old one's status line.
- State the relevant responsibility IDs (R1–R6) and milestone IDs (M01–M08).
- Do not include unmeasured metrics or results; mark anything expected or hypothesised as such.

## Template

```markdown
# NNNN. Title

- Status: Proposed
- Date: YYYY-MM-DD
- Responsibilities: R?
- Milestones: M??

## Context
What problem or question forces a decision? What constraints apply?

## Decision
What we decided, stated plainly.

## Alternatives considered
Each option and why it was not chosen.

## Consequences
What becomes easier or harder; follow-up work; risks and limitations.
```

## Index

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-unified-milestone-numbering.md) | Unified M01–M08 milestone numbering | Accepted |
