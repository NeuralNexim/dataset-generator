from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.validation import validate_sample


def generate_one_sample(domain: str):
    """
    Main entrypoint for sample generation.
    Uses DOMAIN_REGISTRY for all domains.
    Special-cases 'mixed' to avoid circular imports.
    """

    if domain not in DOMAIN_REGISTRY:
        raise ValueError(
            f"Unknown domain: {domain}. Available: {list(DOMAIN_REGISTRY.keys())}"
        )

    if domain == "mixed":
        sample = DOMAIN_REGISTRY["mixed"](DOMAIN_REGISTRY)
        validate_sample(sample, domain="mixed")
        return sample

    sample = DOMAIN_REGISTRY[domain]()
    validate_sample(sample, domain=domain)
    return sample


def generate_dataset(domain: str, n: int):
    if n < 1:
        raise ValueError("n must be >= 1")
    return [generate_one_sample(domain) for _ in range(n)]


def generate_from_cli(args):
    return generate_dataset(domain=args.domain, n=args.count)
