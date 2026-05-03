"""
Multi-step Algebra Domain
Two-step linear equations: ax + b = c, and systems of two equations.
"""

import random

from math_dataset_generator.validation import assert_valid_answer


def generate_multi_step_algebra_sample() -> dict:
    pattern = random.choice(["two_step", "substitution"])

    if pattern == "two_step":
        # ax + b = c  →  x = (c - b) / a
        a = random.randint(2, 8)
        x = random.randint(1, 12)
        b = random.randint(1, 20)
        c = a * x + b
        answer = x
        question = f"Solve for x: {a}x + {b} = {c}"
        expression = f"({c} - {b}) / {a}"
        reasoning = (
            f"Subtract {b} from both sides: {a}x = {c - b}. "
            f"Divide both sides by {a}: x = {c - b}/{a} = {answer}."
        )

    else:  # substitution — x + y = S, x - y = D
        x = random.randint(2, 15)
        y = random.randint(1, x)  # ensure x >= y so difference >= 0
        s = x + y
        d = x - y
        answer = x  # ask for x
        question = f"Solve the system: x + y = {s} and x - y = {d}. What is x?"
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
    }
