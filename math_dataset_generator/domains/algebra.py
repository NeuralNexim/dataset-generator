"""
Algebra Domain
Generates linear equations of the form ax + b = c.
"""

import random
from typing import Dict, Any
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_algebra_sample(difficulty: str = "medium") -> Dict[str, Any]:
    if difficulty == "easy":
        a = random.randint(1, 5)
        x = random.randint(1, 10)
    elif difficulty == "medium":
        a = random.randint(2, 10)
        x = random.randint(5, 20)
    elif difficulty == "hard":
        a = random.randint(5, 20)
        x = random.randint(10, 50)
    elif difficulty == "olympiad":
        a = random.randint(20, 50)
        x = random.randint(50, 200)
    else:
        return generate_algebra_sample(
            random.choice(["easy", "medium", "hard", "olympiad"])
        )

    b = random.randint(1, 20)
    c = a * x + b

    equation = f"{a}x + {b} = {c}"
    question = get_template("algebra", "_default", difficulty).format(eq=equation)

    assert_valid_answer(x, "algebra")
    return {
        "domain": "algebra",
        "input": question,
        "expression": equation,
        "reasoning": f"{a}x = {c} - {b} = {c - b}, so x = {c - b}/{a} = {x}",
        "answer": x,
        "difficulty": difficulty,
    }
