"""
Algebra Domain
Generates linear equations of the form ax + b = c.
"""

import random
from typing import Dict, Any
from math_dataset_generator.validation import assert_valid_answer


def generate_algebra_sample(difficulty: str = "auto") -> Dict[str, Any]:
    if difficulty == "easy":
        a = random.randint(1, 5)
        x = random.randint(1, 10)
    elif difficulty == "medium":
        a = random.randint(2, 10)
        x = random.randint(5, 20)
    elif difficulty == "hard":
        a = random.randint(5, 20)
        x = random.randint(10, 50)
    else:
        return generate_algebra_sample(random.choice(["easy", "medium", "hard"]))

    b = random.randint(1, 20)
    c = a * x + b

    equation = f"{a}x + {b} = {c}"

    assert_valid_answer(x, "algebra")
    return {
        "domain": "algebra",
        "input": equation,
        "expression": equation,
        "reasoning": f"{a}x = {c} - {b} = {c - b}, so x = {c - b}/{a} = {x}",
        "answer": x,
    }
