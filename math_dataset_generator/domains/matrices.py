"""
Matrices & Linear Algebra Domain
2×2 matrix operations: determinant, trace, scalar multiplication result element.
All answers are integers.
"""

import random

from math_dataset_generator.validation import assert_valid_answer


def _det2(a: int, b: int, c: int, d: int) -> int:
    return a * d - b * c


def generate_matrices_sample() -> dict:
    pattern = random.choice(["determinant", "trace", "scalar_mult"])

    # Generate a 2×2 matrix [[a, b],[c, d]]
    a, b = random.randint(1, 9), random.randint(0, 9)
    c, d = random.randint(0, 9), random.randint(1, 9)

    mat_str = f"[[{a}, {b}], [{c}, {d}]]"

    if pattern == "determinant":
        answer = abs(_det2(a, b, c, d))   # keep non-negative
        raw_det = _det2(a, b, c, d)
        question = f"Find the determinant of the 2×2 matrix {mat_str}. Give the absolute value."
        expression = f"|{a}*{d} - {b}*{c}|"
        reasoning = (
            f"det = {a}×{d} - {b}×{c} = {a*d} - {b*c} = {raw_det}. "
            f"Absolute value = {answer}."
        )

    elif pattern == "trace":
        answer = a + d
        question = f"Find the trace (sum of diagonal elements) of the matrix {mat_str}."
        expression = f"{a} + {d}"
        reasoning = f"Trace = top-left + bottom-right = {a} + {d} = {answer}."

    else:  # scalar_mult — report the (0,0) element after multiplying by k
        k = random.randint(2, 5)
        answer = k * a
        question = (
            f"Multiply the matrix {mat_str} by scalar {k}. "
            f"What is the value of the top-left element of the result?"
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
    }
