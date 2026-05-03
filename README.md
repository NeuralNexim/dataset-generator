![Python](https://img.shields.io/badge/python-3.13-blue.svg)
# Math Dataset Generator

Enterprise-grade, modular math dataset generator for training and evaluating reasoning models.

## Features

- Multiple domains:
  - Arithmetic, algebra, geometry
  - Word numbers (0–99,999, config-driven)
  - Story problems (single-step and multi-step)
  - Units, rates, proportional reasoning
  - Mixed-domain reasoning
- Step-by-step reasoning traces
- Unified invariant enforcement (non-negative answers, finite values, non-empty expressions)
- Deterministic output via `--seed` flag
- Unified exception hierarchy (`DomainError`, `TemplateError`, `ReasoningError`, `SampleValidationError`)
- Fail-fast domain guards — errors surface at the generator level with clear domain context
- Per-domain performance benchmarks (min/max/mean/p95 latency) in stress suite
- Debug logging via `--debug` flag
- Noise injection and difficulty scaling
- Curriculum-ready structure
- JSONL dataset output
- Fully modular utilities and domains
- Enterprise-friendly project layout

## Installation

```bash
pip install -e .[dev]
```

## Running Tests

```bash
.venv\Scripts\python.exe -m pytest tests/
```

## CLI Usage

```bash
python -m math_dataset_generator.generate --domain arithmetic --count 100
python -m math_dataset_generator.generate --domain arithmetic --count 100 --seed 42
python -m math_dataset_generator.generate --domain arithmetic --count 100 --debug
python -m math_dataset_generator.generate --domain arithmetic --count 100 --output output/arithmetic.jsonl
```

## Domain Self-Test

```bash
python -m math_dataset_generator.selftest
python -m math_dataset_generator.selftest --samples 200 --seed 42
```

## Stress Suite

```bash
python -m math_dataset_generator.stress --all --load light
python -m math_dataset_generator.stress --perf --load medium
```

## Project Structure

See `docs/ARCHITECTURE.md` for a detailed overview.

