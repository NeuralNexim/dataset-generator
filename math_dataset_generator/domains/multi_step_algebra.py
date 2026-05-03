"""
Multi-step Algebra Domain
Two-step linear equations: ax + b = c, and systems of two equations.
"""

import random

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_multi_step_algebra_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["two_step", "substitution"])

    if difficulty == "easy":
        a_range = (2, 5)
        x_range = (1, 8)
        b_range = (1, 10)
    elif difficulty == "hard":
        a_range = (5, 20)
        x_range = (10, 50)
        b_range = (20, 100)
    elif difficulty == "olympiad":
        a_range = (10, 50)
        x_range = (50, 200)
        b_range = (50, 500)
    else:  # medium
        a_range = (2, 8)
        x_range = (1, 12)
        b_range = (1, 20)

    if pattern == "two_step":
        # ax + b = c  →  x = (c - b) / a
        a = random.randint(*a_range)
        x = random.randint(*x_range)
        b = random.randint(*b_range)
        c = a * x + b
        answer = x
        question = get_template("multi_step_algebra", "two_step", difficulty).format(
            a=a, b=b, c=c
        )
        expression = f"({c} - {b}) / {a}"
        reasoning = (
            f"Subtract {b} from both sides: {a}x = {c - b}. "
            f"Divide both sides by {a}: x = {c - b}/{a} = {answer}."
        )

    else:  # substitution — x + y = S, x - y = D
        x = random.randint(*x_range)
        y = random.randint(1, x)  # ensure x >= y so difference >= 0
        s = x + y
        d = x - y
        answer = x  # ask for x
        question = get_template(
            "multi_step_algebra", "substitution", difficulty
        ).format(s=s, d=d)
        expression = f"({s} + {d}) / 2"
        reasoning = (
            f"Adding the two equations: 2x = {s} + {d} = {s + d}. "
            f"Divide by 2: x = {answer}."
        )

    assert_valid_answer(answer, "multi_step_algebra")
    return {
        "domain": "multi_step_algebra",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
