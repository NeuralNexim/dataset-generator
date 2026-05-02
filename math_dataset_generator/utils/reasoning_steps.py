def build_reasoning_steps(sample):
    """
    Generate simple reasoning steps for interpretability.
    """

    domain = sample["domain"]
    meta = sample["metadata"]

    if domain == "arithmetic":
        return [
            f"Take {meta['a']} and {meta['b']}.",
            f"Apply operator '{meta['op']}'.",
            f"Compute the result.",
        ]

    if domain == "algebra":
        return [
            f"Equation: {meta['a']}x + {meta['b']} = {meta['c']}.",
            "Subtract b from both sides.",
            "Divide by a to isolate x.",
        ]

    if domain == "geometry":
        if meta["shape"] == "rectangle":
            return ["Area = width × height."]
        if meta["shape"] == "triangle":
            return ["Area = 0.5 × base × height."]

    return ["Solve the problem using standard reasoning."]
