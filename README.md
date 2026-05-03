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
  - Probability, combinatorics, sequences & series
  - Number theory (GCD, LCM, primes, divisibility)
  - Logic puzzles, multi-step algebra
  - Calculus (limits, power-rule derivatives, definite integrals)
  - Matrices & linear algebra (2×2 determinant, trace, scalar mult)
  - Diagram-based word problems (text-only: grid, clock, coordinates)
- Step-by-step reasoning traces
- Unified invariant enforcement (non-negative answers, finite values, non-empty expressions)
- **Difficulty tiers** (`easy` | `medium` | `hard` | `olympiad`) — controls numeric range and problem complexity across all domains via `--difficulty` flag
- **Progressive templates** — per-domain, per-difficulty question phrasings stored in `utils/curriculum_templates.py`; questions vary in vocabulary and formality as difficulty increases (e.g., "What is 3 + 4?" → "Determine the exact value of 3 + 4.")
- **Reasoning depth control** — set `--reasoning-depth` to `brief`, `standard`, `detailed`, or `full` (or `auto` mapped by difficulty) to control explanation verbosity
- **Curriculum schedules** — built-in staged schedules for single-domain progression and weighted mixed-domain progression via API and CLI (`domain_progressive`, `mixed_progressive`)
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
python -m math_dataset_generator.generate --domain algebra --count 50 --difficulty olympiad
python -m math_dataset_generator.generate --domain mixed --count 20 --difficulty hard --seed 7
python -m math_dataset_generator.generate --domain story_multi --count 3 --difficulty hard --reasoning-depth detailed
python -m math_dataset_generator.generate --domain algebra --count 100 --curriculum domain_progressive --output output/algebra_curriculum.jsonl
python -m math_dataset_generator.generate --domain mixed --count 100 --curriculum mixed_progressive --seed 42 --output output/mixed_curriculum.jsonl
```

## Curriculum Schedules (API and CLI)

```python
from math_dataset_generator.generator import generate_dataset

# Domain-specific progression: easy -> medium -> hard -> olympiad
rows = generate_dataset("algebra", 100, seed=42, curriculum_schedule="domain_progressive")

# Mixed-domain progression with stage-based weighted source domains
rows = generate_dataset("mixed", 100, seed=42, curriculum_schedule="mixed_progressive")
```

CLI equivalent:

```bash
python -m math_dataset_generator.generate --domain mixed --count 100 --curriculum mixed_progressive --seed 42
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

