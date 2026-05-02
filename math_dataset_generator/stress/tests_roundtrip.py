import random
import time
from typing import Dict, Any
from tqdm import tqdm

from math_dataset_generator.utils.word_to_number import (
    number_to_words,
    words_to_number,
)
from math_dataset_generator.utils.config import CONFIG


def run_roundtrip_tests(
    iterations: int,
    languages: tuple[str, ...],
) -> Dict[str, Any]:
    failures = 0
    start = time.perf_counter()

    for _ in tqdm(range(iterations), desc="Roundtrip", leave=False):
        for lang in languages:
            max_n = CONFIG["languages"][lang]["max_number"]
            n = random.randint(0, min(max_n, 999_999))
            try:
                words = number_to_words(n, lang=lang)
                back = words_to_number(words, lang=lang)
                if back != n:
                    failures += 1
            except Exception:
                failures += 1

    duration = time.perf_counter() - start
    return {
        "name": "roundtrip",
        "iterations": iterations * len(languages),
        "failures": failures,
        "duration_sec": duration,
    }
