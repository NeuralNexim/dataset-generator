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
pytest
```

## CLI Usage

```bash
python -m math_dataset_generator.main --help
```

Example:

```bash
python -m math_dataset_generator.main --domain arithmetic --n 1000 --output output/arithmetic.jsonl
```

## Project Structure

See `docs/ARCHITECTURE.md` for a detailed overview.

