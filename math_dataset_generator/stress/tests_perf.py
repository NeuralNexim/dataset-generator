import time
from typing import Dict, Any, Callable
from tqdm import tqdm


def run_perf_tests(
    iterations: int,
    domains: tuple[str, ...],
    generate_one: Callable[[str], dict],
) -> Dict[str, Any]:
    """
    Performance stress test:
    - Measures throughput
    - Measures average generation time
    - Uses all configured domains
    """
    start = time.perf_counter()
    total = 0

    for _ in tqdm(range(iterations), desc="Perf", leave=False):
        for domain in domains:
            generate_one(domain)
            total += 1

    duration = time.perf_counter() - start
    avg = duration / max(1, total)

    return {
        "name": "perf",
        "iterations": total,
        "failures": 0,
        "duration_sec": duration,
        "avg_sec_per_sample": avg,
    }
