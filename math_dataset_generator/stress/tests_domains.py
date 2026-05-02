import time
from typing import Dict, Any, Callable
from tqdm import tqdm


def run_domain_tests(
    iterations: int,
    domains: tuple[str, ...],
    generate_one: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    failures = 0
    start = time.perf_counter()

    for _ in tqdm(range(iterations), desc="Domains", leave=False):
        for domain in domains:
            try:
                sample = generate_one(domain)
                if not isinstance(sample, dict):
                    failures += 1
                    continue
                for key in ("domain", "input", "expression", "reasoning", "answer"):
                    if key not in sample:
                        failures += 1
                        break
            except Exception:
                failures += 1

    duration = time.perf_counter() - start
    return {
        "name": "domains",
        "iterations": iterations * len(domains),
        "failures": failures,
        "duration_sec": duration,
    }
