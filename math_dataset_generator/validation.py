import math

from math_dataset_generator.exceptions import (
    DomainError,
    SampleValidationError,
)  # noqa: F401

REQUIRED_FIELDS = ["domain", "input", "expression", "reasoning", "answer"]

DIFFICULTY_LEVELS = ("easy", "medium", "hard", "olympiad")

VALID_UNITS = {
    "km",
    "m",
    "cm",
    "mm",
    "kg",
    "g",
    "mg",
    "l",
    "ml",
    "km/h",
    "m/s",
    "hours",
    "minutes",
    "seconds",
}

# Declarative invariants per domain — used for documentation and future
# per-domain validation extensions.
DOMAIN_INVARIANTS: dict[str, dict] = {
    "arithmetic": {"answer_min": 0, "answer_type": (int,)},
    "algebra": {"answer_min": 0, "answer_type": (int,)},
    "geometry": {"answer_min": 0, "answer_type": (int, float)},
    "word_numbers": {"answer_min": 0, "answer_type": (int,)},
    "story_single": {"answer_min": 0, "answer_type": (int,)},
    "story_multi": {"answer_min": 0, "answer_type": (int,)},
    "units_rates": {"answer_min": 0, "answer_type": (int, float)},
    "proportional": {"answer_min": 0, "answer_type": (int,)},
    "functions": {"answer_min": 0, "answer_type": (int,)},
    "mixed": {"answer_min": 0, "answer_type": (int, float)},
    # Section 2: New Domains
    "probability": {"answer_min": 0, "answer_type": (float,)},
    "combinatorics": {"answer_min": 0, "answer_type": (int,)},
    "sequences": {"answer_min": 0, "answer_type": (int,)},
    "number_theory": {"answer_min": 0, "answer_type": (int,)},
    "logic_puzzles": {"answer_min": 0, "answer_type": (int,)},
    "multi_step_algebra": {"answer_min": 0, "answer_type": (int,)},
    "calculus": {"answer_min": 0, "answer_type": (int,)},
    "matrices": {"answer_min": 0, "answer_type": (int,)},
    "diagram_word_problems": {"answer_min": 0, "answer_type": (int,)},
}


def assert_valid_answer(answer: object, domain: str) -> None:
    """Fail-fast guard for use inside domain generators.

    Raises DomainError so the call stack clearly points to the offending
    domain function.
    """
    if not isinstance(answer, (int, float)):
        raise DomainError(
            f"[{domain}] answer must be int or float, got {type(answer).__name__}: {answer!r}"
        )
    if isinstance(answer, float) and not math.isfinite(answer):
        raise DomainError(f"[{domain}] answer is not finite: {answer}")
    if answer < 0:
        raise DomainError(f"[{domain}] answer must be >= 0, got {answer}")


def _check_invariants(sample: dict) -> None:
    """Enforce cross-domain invariants on a validated sample."""
    answer = sample.get("answer")

    if not isinstance(answer, (int, float)):
        raise SampleValidationError(
            f"Answer must be a number, got {type(answer).__name__}: {answer!r}"
        )
    if isinstance(answer, float) and not math.isfinite(answer):
        raise SampleValidationError(f"Answer must be finite, got {answer}")
    if answer < 0:
        raise SampleValidationError(f"Answer must be >= 0, got {answer}")

    expression = sample.get("expression", "")
    if not isinstance(expression, str) or not expression.strip():
        raise SampleValidationError(
            f"Expression must be a non-empty string, got {expression!r}"
        )


def validate_sample(sample: dict, domain: str | None = None) -> None:
    if not isinstance(sample, dict):
        raise SampleValidationError(f"Sample must be dict, got {type(sample)}")

    for field in REQUIRED_FIELDS:
        if field not in sample:
            raise SampleValidationError(f"Missing field '{field}' in sample: {sample}")

    if domain is not None and sample.get("domain") not in {domain, "mixed"}:
        raise SampleValidationError(
            f"Sample domain '{sample.get('domain')}' does not match requested '{domain}'"
        )

    difficulty = sample.get("difficulty")
    if difficulty is not None and difficulty not in DIFFICULTY_LEVELS:
        raise SampleValidationError(
            f"Invalid difficulty '{difficulty}'. Must be one of {DIFFICULTY_LEVELS}"
        )

    _check_invariants(sample)
