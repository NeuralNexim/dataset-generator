def build_expression(sample: dict) -> str | None:
    """Build a symbolic expression from a dataset sample.

    Primary path: use ``sample['metadata']`` if present.
    Fallback: return the ``sample['expression']`` string already set by the domain.
    Returns None only if neither source is available.
    """
    # Fast path: domain already set a direct expression string
    direct = sample.get("expression")
    if not isinstance(sample.get("metadata"), dict):
        return direct if isinstance(direct, str) and direct.strip() else None

    meta = sample["metadata"]

    if sample["domain"] == "arithmetic":
        return f"{meta['a']} {meta['op']} {meta['b']}"

    if sample["domain"] == "algebra":
        return f"{meta['a']}*x + {meta['b']} = {meta['c']}"

    if sample["domain"] == "geometry":
        if meta.get("shape") == "rectangle":
            return f"{meta['w']} * {meta['h']}"
        if meta.get("shape") == "triangle":
            return f"0.5 * {meta['b']} * {meta['h']}"

    # Metadata present but domain not handled — fall back to direct expression
    return direct if isinstance(direct, str) and direct.strip() else None
