import math

REQUIRED_FIELDS = ["domain", "input", "expression", "reasoning", "answer"]

VALID_UNITS = {
    "km", "m", "cm", "mm",
    "kg", "g", "mg",
    "l", "ml",
    "km/h", "m/s",
    "hours", "minutes", "seconds",
}


class SampleValidationError(Exception):
    pass


def _check_invariants(sample: dict) -> None:
    """Enforce cross-domain invariants on a validated sample."""
    answer = sample.get("answer")

    # Answer must be a finite number
    if not isinstance(answer, (int, float)):
        raise SampleValidationError(
            f"Answer must be a number, got {type(answer).__name__}: {answer!r}"
        )
    if isinstance(answer, float) and not math.isfinite(answer):
        raise SampleValidationError(
            f"Answer must be finite, got {answer}"
        )

    # Answer must not be negative
    if answer < 0:
        raise SampleValidationError(
            f"Answer must be >= 0, got {answer}"
        )

    # Expression must be a non-empty string
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

    _check_invariants(sample)
