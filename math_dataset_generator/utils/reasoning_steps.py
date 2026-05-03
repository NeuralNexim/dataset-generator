from math_dataset_generator.exceptions import ReasoningError


def build_reasoning_steps(sample: dict) -> list[str]:
    """Generate reasoning steps for a sample.

    Primary path: use ``sample['metadata']`` for structured step generation.
    Fallback: split the sample's own ``reasoning`` string into a single-item list.
    Raises ReasoningError only if neither metadata nor reasoning string is available.
    """
    domain = sample.get("domain")
    if not domain:
        raise ReasoningError("sample is missing 'domain' field")

    meta = sample.get("metadata")

    if not isinstance(meta, dict):
        # Fallback: wrap the domain-generated reasoning string
        reasoning = sample.get("reasoning", "")
        if reasoning:
            return [reasoning]
        raise ReasoningError(
            f"[{domain}] no 'metadata' dict and no 'reasoning' string available"
        )

    if domain == "arithmetic":
        return [
            f"Take {meta['a']} and {meta['b']}.",
            f"Apply operator '{meta['op']}'.",
            "Compute the result.",
        ]

    if domain == "algebra":
        return [
            f"Equation: {meta['a']}x + {meta['b']} = {meta['c']}.",
            "Subtract b from both sides.",
            "Divide by a to isolate x.",
        ]

    if domain == "geometry":
        if meta.get("shape") == "rectangle":
            return ["Area = width × height."]
        if meta.get("shape") == "triangle":
            return ["Area = 0.5 × base × height."]

    return [sample.get("reasoning", "Solve the problem using standard reasoning.")]
