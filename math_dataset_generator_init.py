import os

ROOT = "math_dataset_generator"

# Folder structure
FOLDERS = [
    ROOT,
    f"{ROOT}/domains",
    f"{ROOT}/utils",
    "tests",
    "output",
]

# Auto-populated file contents
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

[tool.setuptools.packages.find]
where = ["."]
include = ["math_dataset_generator*"]

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
"""

README = """\
# Math Dataset Generator

A modular, multi-domain dataset generator for arithmetic, algebra, geometry,
word numbers, story problems, proportional reasoning, and mixed-domain reasoning.

## Features
- Symbolic expression extraction
- Step-by-step reasoning
- Noise injection
- Difficulty scaling
- Curriculum-ready architecture
- JSONL dataset output
- Fully modular domain system

## Usage
# pip install -e .
# python -m math_dataset_generator.main --domain arithmetic --n 1000
"""

REQUIREMENTS = """\
pytest
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

CONFIG = "MAX_WORD_NUMBER = 99999\n"

MAIN_TEMPLATE = """\
def main():
    print("Math Dataset Generator entry point.")

if __name__ == "__main__":
    main()
"""

STRESS_GENERATORS = """\
from .config import MAX_WORD_NUMBER
from .randomizers import number_to_words
from .word_to_number import words_to_number
import random

def generate_word_number_stress_cases(count=1000, seed=None):
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
            "ok": (n == back)
        })
    return cases
"""

# Files to create
FILES = {
    # Root package
    f"{ROOT}/__init__.py": "",
    f"{ROOT}/main.py": MAIN_TEMPLATE,

    # Config
    f"{ROOT}/utils/config.py": CONFIG,

    # Domain modules (empty placeholders)
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
}


def create_structure():
    print("\n=== Creating Project Structure ===\n")

    # Create folders
    for folder in FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✔️  Created folder: {folder}")
        else:
            print(f"⚠️  Folder already exists: {folder}")

    print()

    # Create files
    for filepath, content in FILES.items():
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✔️  Created file: {filepath}")
        else:
            print(f"⚠️  File already exists: {filepath}")

    print("\n=== Done ===\n")


if __name__ == "__main__":
    create_structure()
