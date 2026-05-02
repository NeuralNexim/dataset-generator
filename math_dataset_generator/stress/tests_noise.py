import time
from typing import Dict, Any
from tqdm import tqdm

from math_dataset_generator.utils.noise import apply_noise


def run_noise_tests(iterations: int) -> Dict[str, Any]:
    failures = 0
    start = time.perf_counter()
    levels = ["light", "medium", "heavy"]

    for _ in tqdm(range(iterations), desc="Noise", leave=False):
        text = f"Base text {_}"
        for level in levels:
            try:
                out = apply_noise(text, level)  # type: ignore[arg-type]
                if not isinstance(out, str):
                    failures += 1
            except Exception:
                failures += 1

    duration = time.perf_counter() - start
    return {
        "name": "noise",
        "iterations": iterations * len(levels),
        "failures": failures,
        "duration_sec": duration,
    }
