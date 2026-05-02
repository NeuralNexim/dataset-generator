from typing import Dict, Any, Tuple
from math_dataset_generator.utils.config import CONFIG


def resolve_load(
    load: str,
    iterations_override: int | None = None,
) -> Dict[str, int]:
    """
    Map load level name to iteration counts for each test type.
    """
    levels: Dict[str, Dict[str, int]] = CONFIG.get("stress_levels", {})
    if load == "custom":
        if iterations_override is None:
            raise ValueError("Custom load requires --iterations")
        return {
            "roundtrip": iterations_override,
            "noise": iterations_override,
            "domains": iterations_override,
            "templates": iterations_override,
            "perf": iterations_override,
        }

    if load not in levels:
        raise ValueError(f"Unknown load level: {load}")

    return levels[load]


def get_stress_domains() -> Tuple[str, ...]:
    domains = CONFIG.get("stress_domains", [])
    return tuple(domains)


def get_stress_languages() -> Tuple[str, ...]:
    langs = CONFIG.get("default_languages", ["en"])
    return tuple(langs)
