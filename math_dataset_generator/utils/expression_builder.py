def build_expression(sample):
    """
    Build a symbolic expression from a dataset sample.
    Domains may override this later.
    """
    if "metadata" not in sample:
        return None

    meta = sample["metadata"]

    if sample["domain"] == "arithmetic":
        return f"{meta['a']} {meta['op']} {meta['b']}"

    if sample["domain"] == "algebra":
        return f"{meta['a']}*x + {meta['b']} = {meta['c']}"

    if sample["domain"] == "geometry":
        if meta["shape"] == "rectangle":
            return f"{meta['w']} * {meta['h']}"
        if meta["shape"] == "triangle":
            return f"0.5 * {meta['b']} * {meta['h']}"

    return None
