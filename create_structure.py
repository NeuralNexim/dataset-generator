import os
import textwrap
import argparse

ROOT = "math_dataset_generator"

# -----------------------------
# Folder structure
# -----------------------------
FOLDERS = [
    ROOT,
    f"{ROOT}/domains",
    f"{ROOT}/utils",
    "tests",
    "output",
    ".vscode",
    ".github",
    ".github/ISSUE_TEMPLATE",
    "docs",
]

# -----------------------------
# File templates
# -----------------------------

PYPROJECT = """\
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "math_dataset_generator"
version = "0.1.0"
description = "A modular math dataset generator with multi-domain reasoning."
authors = [
    { name = "Jeyakumar Sethuram" }
]
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest",
    "black",
    "ruff",
    "mypy"
]
train = [
    "torch",
    "transformers",
    "datasets",
    "accelerate",
    "sentencepiece"
]

[tool.setuptools.packages.find]
where = ["."]
include = ["math_dataset_generator*"]

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
addopts = "-q"

[tool.black]
line-length = 88
target-version = ["py313"]

[tool.ruff]
line-length = 88
target-version = "py313"
select = ["E", "F", "I"]

[tool.mypy]
python_version = "3.13"
ignore_missing_imports = true
"""

README = """\
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
"""

REQUIREMENTS = """\
pytest
black
ruff
mypy
"""

GITIGNORE = """\
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
*.egg-info/
.eggs/
dist/
build/

# Virtual env
.venv/
venv/

# IDE
.vscode/
.idea/

# Pytest
.pytest_cache/

# Output
output/
"""

VS_CODE_SETTINGS = """\
{
    "python.defaultInterpreterPath": ".venv/Scripts/python.exe",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
    }
}
"""

ISSUE_TEMPLATE_BUG = """\
name: Bug report
about: Report a bug in math-dataset-generator
labels: bug
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What happened?
    validations:
      required: true
"""

ISSUE_TEMPLATE_FEATURE = """\
name: Feature request
about: Suggest an idea for math-dataset-generator
labels: enhancement
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What would you like to see?
    validations:
      required: true
"""

PULL_REQUEST_TEMPLATE = """\
# Summary

Describe the changes in this PR.

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Refactor
- [ ] Documentation

## Testing

- [ ] `pytest`
"""

ARCHITECTURE = """\
# Architecture

```mermaid
flowchart TD
    A[main.py] --> B[domains]
    A --> C[utils]
    B --> B1[arithmetic.py]
    B --> B2[algebra.py]
    B --> B3[geometry.py]
    B --> B4[word_numbers.py]
    B --> B5[story_single_step.py]
    B --> B6[story_multi_step.py]
    B --> B7[units_rates.py]
    B --> B8[proportional.py]
    B --> B9[mixed_domain.py]
    C --> C1[randomizers.py]
    C --> C2[expression_builder.py]
    C --> C3[reasoning_steps.py]
    C --> C4[templates.py]
    C --> C5[noise.py]
    C --> C6[word_to_number.py]
    C --> C7[stress_generators.py]
    C --> C8[config.py]
```

- `math_dataset_generator/main.py`:
  - CLI entry point
  - Dispatches to domains
- `math_dataset_generator/domains/`:
  - Each file implements a domain-specific generator
- `math_dataset_generator/utils/`:
  - Shared utilities for randomization, expressions, reasoning, noise, config
- `tests/`:
  - Unit tests for core utilities and domains
"""

CHANGELOG = """\
# Changelog

## 0.1.0

- Initial enterprise-grade project structure
- Word-number support 0–99,999 with config-driven max
- Basic tests and tooling
"""

CONFIG = "MAX_WORD_NUMBER = 99999\n"

MAIN_TEMPLATE = """\
import argparse
from typing import Optional

def generate_dataset(domain: str, n: int, output: Optional[str] = None):
    # TODO: wire this to actual domain generators
    print(f"Generating {n} samples for domain '{domain}'")
    if output:
        print(f"Would write to: {output}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Math Dataset Generator - multi-domain reasoning datasets."
    )
    parser.add_argument(
        "--domain",
        type=str,
        required=True,
        help="Domain to generate (e.g., arithmetic, algebra, geometry, word_numbers, story_single_step, ...).",
    )
    parser.add_argument(
        "--n",
        type=int,
        required=True,
        help="Number of samples to generate.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional output file path (e.g., output/arithmetic.jsonl).",
    )
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    generate_dataset(domain=args.domain, n=args.n, output=args.output)

if __name__ == "__main__":
    main()
"""

STRESS_GENERATORS = """\
from .config import MAX_WORD_NUMBER
from .randomizers import number_to_words
from .word_to_number import words_to_number
import random

def generate_word_number_stress_cases(count: int = 1000, seed: int | None = None):
    if seed is not None:
        random.seed(seed)

    cases = []
    for _ in range(count):
        n = random.randint(0, MAX_WORD_NUMBER)
        words = number_to_words(n)
        back = words_to_number(words)
        cases.append({
            "n": n,
            "words": words,
            "back": back,
            "ok": (n == back),
        })
    return cases
"""

TEST_WORD_NUMBERS = """\
from math_dataset_generator.utils.word_to_number import words_to_number
from math_dataset_generator.utils.randomizers import number_to_words
from math_dataset_generator.utils.config import MAX_WORD_NUMBER

def test_roundtrip_small():
    for n in range(0, min(1000, MAX_WORD_NUMBER + 1)):
        words = number_to_words(n)
        back = words_to_number(words)
        assert back == n

def test_specific_cases():
    cases = {
        "zero": 0,
        "twenty one": 21,
        "one hundred and five": 105,
        "nine thousand nine hundred ninety nine": 9999,
    }
    for text, expected in cases.items():
        assert words_to_number(text) == expected
"""

MAKEFILE = """\
.PHONY: test lint format typecheck run clean

test:
\tpytest

lint:
\truff math_dataset_generator tests

format:
\tblack math_dataset_generator tests

typecheck:
\tmypy math_dataset_generator

run:
\tpython -m math_dataset_generator.main --domain arithmetic --n 10

clean:
\trm -rf .pytest_cache
\trm -rf build dist *.egg-info
"""

# -----------------------------
# Files to create
# -----------------------------
FILES = {
    # Root package
    f"{ROOT}/__init__.py": "",
    f"{ROOT}/main.py": MAIN_TEMPLATE,
    # Config
    f"{ROOT}/utils/config.py": CONFIG,
    # Domain modules (placeholders)
    f"{ROOT}/domains/__init__.py": "",
    f"{ROOT}/domains/arithmetic.py": "",
    f"{ROOT}/domains/functions.py": "",
    f"{ROOT}/domains/word_numbers.py": "",
    f"{ROOT}/domains/story_single_step.py": "",
    f"{ROOT}/domains/story_multi_step.py": "",
    f"{ROOT}/domains/units_rates.py": "",
    f"{ROOT}/domains/proportional.py": "",
    f"{ROOT}/domains/geometry.py": "",
    f"{ROOT}/domains/algebra.py": "",
    f"{ROOT}/domains/mixed_domain.py": "",
    # Utility modules
    f"{ROOT}/utils/__init__.py": "",
    f"{ROOT}/utils/noise.py": "",
    f"{ROOT}/utils/word_to_number.py": "",
    f"{ROOT}/utils/expression_builder.py": "",
    f"{ROOT}/utils/reasoning_steps.py": "",
    f"{ROOT}/utils/randomizers.py": "",
    f"{ROOT}/utils/templates.py": "",
    f"{ROOT}/utils/stress_generators.py": STRESS_GENERATORS,
    # Tests
    "tests/__init__.py": "",
    "tests/test_word_numbers.py": TEST_WORD_NUMBERS,
    # Project files
    "pyproject.toml": PYPROJECT,
    "README.md": README,
    "requirements.txt": REQUIREMENTS,
    ".gitignore": GITIGNORE,
    "Makefile": MAKEFILE,
    # VS Code
    ".vscode/settings.json": VS_CODE_SETTINGS,
    # GitHub templates
    ".github/ISSUE_TEMPLATE/bug_report.yml": ISSUE_TEMPLATE_BUG,
    ".github/ISSUE_TEMPLATE/feature_request.yml": ISSUE_TEMPLATE_FEATURE,
    ".github/pull_request_template.md": PULL_REQUEST_TEMPLATE,
    # Docs
    "docs/ARCHITECTURE.md": ARCHITECTURE,
    "docs/CHANGELOG.md": CHANGELOG,
}

# ---------------------------------------------------------
# Your existing FOLDERS and FILES dictionaries stay the same
# ---------------------------------------------------------


def create_structure(force: bool = False):
    print("\n=== Creating Project Structure ===\n")

    # Create folders
    for folder in FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✔️  Created folder: {folder}")
        else:
            print(f"⚠️  Folder already exists: {folder}")

    print()

    # Create or overwrite files
    for filepath, content in FILES.items():
        exists = os.path.exists(filepath)

        if exists and not force:
            print(f"⚠️  File already exists: {filepath}")
            continue

        # Write file (overwrite if force=True)
        text = textwrap.dedent(content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

        if exists and force:
            print(f"🔁 Overwritten: {filepath}")
        else:
            print(f"✔️  Created file: {filepath}")

    print("\n=== Done ===\n")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Project scaffold generator (safe by default)."
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Overwrite existing files with template versions.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    create_structure(force=args.force)
