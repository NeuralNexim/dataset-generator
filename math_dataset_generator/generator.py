import random

from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.utils.curriculum_schedules import resolve_curriculum_stage
from math_dataset_generator.utils.reasoning_steps import apply_reasoning_depth
from math_dataset_generator.validation import validate_sample
from math_dataset_generator.utils.logger import get_logger

_log = get_logger(__name__)


def _generate_weighted_mixed_sample(
    domain_weights: dict[str, int], difficulty: str, reasoning_depth: str
):
    available_domains = {
        d: w
        for d, w in domain_weights.items()
        if d in DOMAIN_REGISTRY and d != "mixed" and w > 0
    }
    if not available_domains:
        raise ValueError("Curriculum stage has no valid positive mixed-domain weights")

    domains = list(available_domains.keys())
    weights = list(available_domains.values())
    source_domain = random.choices(domains, weights=weights, k=1)[0]

    sample = generate_one_sample(
        source_domain, difficulty=difficulty, reasoning_depth=reasoning_depth
    )
    sample["source_domain"] = source_domain
    sample["domain"] = "mixed"
    return sample


def generate_one_sample(
    domain: str, difficulty: str = "medium", reasoning_depth: str = "auto"
):
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
        sample = DOMAIN_REGISTRY["mixed"](DOMAIN_REGISTRY, difficulty=difficulty)
        sample = apply_reasoning_depth(
            sample, depth=reasoning_depth, difficulty=difficulty
        )
        validate_sample(sample, domain="mixed")
        _log.debug("generated mixed sample: answer=%s", sample.get("answer"))
        return sample

    sample = DOMAIN_REGISTRY[domain](difficulty=difficulty)
    sample = apply_reasoning_depth(sample, depth=reasoning_depth, difficulty=difficulty)
    validate_sample(sample, domain=domain)
    _log.debug("generated %s sample: answer=%s", domain, sample.get("answer"))
    return sample


def generate_dataset(
    domain: str,
    n: int,
    seed: int | None = None,
    difficulty: str = "medium",
    reasoning_depth: str = "auto",
    curriculum_schedule: str | None = None,
):
    if n < 1:
        raise ValueError("n must be >= 1")
    if seed is not None:
        random.seed(seed)
    samples = []
    for i in range(n):
        sample_difficulty = difficulty
        sample_reasoning_depth = reasoning_depth
        stage_name = None
        stage_weights = None

        if curriculum_schedule:
            stage = resolve_curriculum_stage(curriculum_schedule, i, n)
            sample_difficulty = stage.difficulty
            stage_name = stage.name
            if stage.reasoning_depth is not None:
                sample_reasoning_depth = stage.reasoning_depth
            stage_weights = stage.domain_weights

        if domain == "mixed" and stage_weights:
            sample = _generate_weighted_mixed_sample(
                stage_weights,
                difficulty=sample_difficulty,
                reasoning_depth=sample_reasoning_depth,
            )
            validate_sample(sample, domain="mixed")
        else:
            sample = generate_one_sample(
                domain,
                difficulty=sample_difficulty,
                reasoning_depth=sample_reasoning_depth,
            )

        if stage_name:
            sample["curriculum_stage"] = stage_name
        samples.append(sample)

    return samples


def generate_from_cli(args):
    n = getattr(args, "n", None) or getattr(args, "count", 1)
    seed = getattr(args, "seed", None)
    difficulty = getattr(args, "difficulty", "medium") or "medium"
    reasoning_depth = getattr(args, "reasoning_depth", "auto") or "auto"
    return generate_dataset(
        domain=args.domain,
        n=n,
        seed=seed,
        difficulty=difficulty,
        reasoning_depth=reasoning_depth,
        curriculum_schedule=getattr(args, "curriculum_schedule", None),
    )
