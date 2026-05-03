import time
import statistics
from typing import Dict, Any, Callable
from tqdm import tqdm


def _p95(data: list[float]) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    idx = max(0, int(len(sorted_data) * 0.95) - 1)
    return sorted_data[idx]


def run_perf_tests(
    iterations: int,
    domains: tuple[str, ...],
    generate_one: Callable[[str], dict],
) -> Dict[str, Any]:
    """
    Performance stress test:
    - Measures throughput (samples/sec)
    - Per-domain min/max/mean/p95 latency
    """
    domain_times: Dict[str, list[float]] = {d: [] for d in domains}
    total = 0

    wall_start = time.perf_counter()
    for _ in tqdm(range(iterations), desc="Perf", leave=False):
        for domain in domains:
            t0 = time.perf_counter()
            generate_one(domain)
            domain_times[domain].append(time.perf_counter() - t0)
            total += 1
    duration = time.perf_counter() - wall_start

    per_domain = {}
    for domain, times in domain_times.items():
        if times:
            per_domain[domain] = {
                "n": len(times),
                "min_ms": round(min(times) * 1000, 4),
                "max_ms": round(max(times) * 1000, 4),
                "mean_ms": round(statistics.mean(times) * 1000, 4),
                "p95_ms": round(_p95(times) * 1000, 4),
            }

    return {
        "name": "perf",
        "iterations": total,
        "failures": 0,
        "duration_sec": duration,
        "avg_sec_per_sample": duration / max(1, total),
        "throughput_per_sec": round(total / max(1e-9, duration), 2),
        "per_domain": per_domain,
    }
