REQUIRED_FIELDS = ["domain", "input", "expression", "reasoning", "answer"]


class SampleValidationError(Exception):
    pass


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
