"""
Matrices & Linear Algebra Domain
2×2 matrix operations: determinant, trace, scalar multiplication result element.
All answers are integers.
"""

import random

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def _det2(a: int, b: int, c: int, d: int) -> int:
    return a * d - b * c


def generate_matrices_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["determinant", "trace", "scalar_mult"])

    # Generate a 2×2 matrix [[a, b],[c, d]]
    if difficulty == "easy":
        lo, hi = 1, 5
        k_range = (2, 3)
    elif difficulty == "hard":
        lo, hi = 1, 15
        k_range = (3, 8)
    elif difficulty == "olympiad":
        lo, hi = 5, 20
        k_range = (5, 15)
    else:  # medium
        lo, hi = 1, 9
        k_range = (2, 5)

    a, b = random.randint(lo, hi), random.randint(0, hi)
    c, d = random.randint(0, hi), random.randint(lo, hi)

    mat_str = f"[[{a}, {b}], [{c}, {d}]]"

    if pattern == "determinant":
        answer = abs(_det2(a, b, c, d))  # keep non-negative
        raw_det = _det2(a, b, c, d)
        question = get_template("matrices", "determinant", difficulty).format(
            mat=mat_str
        )
        expression = f"|{a}*{d} - {b}*{c}|"
        reasoning = (
            f"det = {a}×{d} - {b}×{c} = {a*d} - {b*c} = {raw_det}. "
            f"Absolute value = {answer}."
        )

    elif pattern == "trace":
        answer = a + d
        question = get_template("matrices", "trace", difficulty).format(mat=mat_str)
        expression = f"{a} + {d}"
        reasoning = f"Trace = top-left + bottom-right = {a} + {d} = {answer}."

    else:  # scalar_mult — report the (0,0) element after multiplying by k
        k = random.randint(*k_range)
        answer = k * a
        question = get_template("matrices", "scalar_mult", difficulty).format(
            mat=mat_str, k=k
        )
        expression = f"{k} * {a}"
        reasoning = f"Scalar multiplication: {k} × {a} = {answer}."

    assert_valid_answer(answer, "matrices")
    return {
        "domain": "matrices",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
