import re

from math_dataset_generator.exceptions import ReasoningError

_REASONING_DEPTHS = ("auto", "brief", "standard", "detailed", "full")


def _split_reasoning_text(reasoning: str) -> list[str]:
    """Split a free-form reasoning string into coarse steps."""
    if not reasoning:
        return []

    steps = [
        part.strip() for part in re.split(r"(?<=[.!?])\s+", reasoning) if part.strip()
    ]
    if len(steps) <= 1:
        steps = [part.strip() for part in reasoning.split(";") if part.strip()]
    if not steps:
        return [reasoning.strip()]
    return steps


def _resolve_reasoning_depth(depth: str, difficulty: str) -> str:
    if depth not in _REASONING_DEPTHS:
        return "standard"
    if depth != "auto":
        return depth

    mapping = {
        "easy": "brief",
        "medium": "standard",
        "hard": "detailed",
        "olympiad": "full",
    }
    return mapping.get(difficulty, "standard")


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
            return _split_reasoning_text(reasoning)
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

    return _split_reasoning_text(
        sample.get("reasoning", "Solve the problem using standard reasoning.")
    )


def apply_reasoning_depth(
    sample: dict, depth: str = "auto", difficulty: str = "medium"
) -> dict:
    """Adjust reasoning verbosity while preserving the sample schema."""
    try:
        steps = build_reasoning_steps(sample)
    except ReasoningError:
        return sample

    if not steps:
        return sample

    resolved = _resolve_reasoning_depth(depth, difficulty)

    if resolved == "brief":
        selected = [steps[-1]]
        sample["reasoning"] = selected[0]
        return sample

    if resolved == "standard":
        selected = steps if len(steps) <= 2 else [steps[0], steps[-1]]
        sample["reasoning"] = " ".join(selected)
        return sample

    cleaned_steps = [re.sub(r"^Step\s+\d+:\s*", "", step).strip() for step in steps]
    numbered = [f"Step {i + 1}: {step}" for i, step in enumerate(cleaned_steps)]
    if resolved == "detailed":
        sample["reasoning"] = " ".join(numbered)
        return sample

    # full
    answer = sample.get("answer")
    sample["reasoning"] = " ".join(numbered) + f" Final answer: {answer}."
    return sample
