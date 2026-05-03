import random

from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.validation import validate_sample
from math_dataset_generator.utils.logger import get_logger

_log = get_logger(__name__)


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
        _log.debug("generated mixed sample: answer=%s", sample.get("answer"))
        return sample

    sample = DOMAIN_REGISTRY[domain]()
    validate_sample(sample, domain=domain)
    _log.debug("generated %s sample: answer=%s", domain, sample.get("answer"))
    return sample


def generate_dataset(domain: str, n: int, seed: int | None = None):
    if n < 1:
        raise ValueError("n must be >= 1")
    if seed is not None:
        random.seed(seed)
    return [generate_one_sample(domain) for _ in range(n)]


def generate_from_cli(args):
    n = getattr(args, "n", None) or getattr(args, "count", 1)
    seed = getattr(args, "seed", None)
    return generate_dataset(domain=args.domain, n=n, seed=seed)
