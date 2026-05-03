import random


def generate_mixed_sample(domain_registry=None, difficulty: str = "medium"):
    """
    Randomly selects a domain and generates a sample from it.
    domain_registry is passed in by the generator to avoid circular imports.
    """

    if domain_registry is None:
        raise ValueError("generate_mixed_sample requires domain_registry passed in.")

    # Avoid recursion: remove mixed itself
    domains = [d for d in domain_registry.keys() if d != "mixed"]

    d = random.choice(domains)
    sample = domain_registry[d](difficulty=difficulty)

    # Override domain label
    sample["domain"] = "mixed"
    sample["source_domain"] = d

    return sample
