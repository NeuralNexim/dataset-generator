import time
from typing import Dict, Any
from tqdm import tqdm

from math_dataset_generator.utils.templates import (
    choose_template,
    render_template,
    choose_name,
    choose_object,
)


def run_template_tests(iterations: int) -> Dict[str, Any]:
    failures = 0
    start = time.perf_counter()
    categories = [
        "story_single",
        "story_multi",
        "units_rates",
        "proportional",
        "geometry",
        "algebra",
        "mixed",
    ]

    for _ in tqdm(range(iterations), desc="Templates", leave=False):
        for cat in categories:
            try:
                tmpl = choose_template(cat)
                text = render_template(
                    tmpl,
                    name=choose_name(),
                    obj=choose_object(),
                    a=1,
                    b=2,
                    c=3,
                    a2=4,
                    w=3,
                    h=5,
                    b2=7,
                    speed=10,
                    time=2,
                    rate=3,
                )
                if not isinstance(text, str) or "{" in text:
                    failures += 1
            except Exception:
                failures += 1

    duration = time.perf_counter() - start
    return {
        "name": "templates",
        "iterations": iterations * len(categories),
        "failures": failures,
        "duration_sec": duration,
    }
