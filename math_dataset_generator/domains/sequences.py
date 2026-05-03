"""
Sequences & Series Domain
Arithmetic sequences (nth term, sum), geometric sequences (nth term).
"""

import random

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_sequences_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["arith_nth", "arith_sum", "geo_nth"])

    if difficulty == "easy":
        a_range = (1, 5)
        d_range = (1, 5)
        n_arith = (3, 8)
        geo_a_range = (1, 3)
        geo_r_range = (2, 3)
        geo_n_range = (2, 5)
    elif difficulty == "hard":
        a_range = (5, 30)
        d_range = (5, 30)
        n_arith = (10, 30)
        geo_a_range = (2, 8)
        geo_r_range = (2, 5)
        geo_n_range = (5, 9)
    elif difficulty == "olympiad":
        a_range = (10, 100)
        d_range = (10, 100)
        n_arith = (20, 50)
        geo_a_range = (3, 10)
        geo_r_range = (3, 6)
        geo_n_range = (6, 10)
    else:  # medium
        a_range = (1, 10)
        d_range = (1, 10)
        n_arith = (5, 15)
        geo_a_range = (1, 5)
        geo_r_range = (2, 4)
        geo_n_range = (3, 7)

    if pattern == "arith_nth":
        a = random.randint(*a_range)
        d = random.randint(*d_range)
        n = random.randint(*n_arith)
        answer = a + (n - 1) * d
        question = get_template("sequences", "arith_nth", difficulty).format(
            a=a, d=d, n=n
        )
        expression = f"{a} + ({n} - 1) * {d}"
        reasoning = (
            f"nth term = a + (n-1)d = {a} + ({n}-1) × {d} = {a} + {(n-1)*d} = {answer}."
        )

    elif pattern == "arith_sum":
        a = random.randint(*a_range)
        d = random.randint(*d_range)
        n = random.randint(*n_arith)
        answer = n * (2 * a + (n - 1) * d) // 2
        question = get_template("sequences", "arith_sum", difficulty).format(
            a=a, d=d, n=n
        )
        expression = f"{n} * (2*{a} + ({n}-1)*{d}) / 2"
        reasoning = f"S = n/2 × (2a + (n-1)d) = {n}/2 × ({2*a} + {(n-1)*d}) = {answer}."

    else:  # geo_nth
        a = random.randint(*geo_a_range)
        r = random.randint(*geo_r_range)
        n = random.randint(*geo_n_range)
        answer = a * (r ** (n - 1))
        question = get_template("sequences", "geo_nth", difficulty).format(
            a=a, r=r, n=n
        )
        expression = f"{a} * {r}^({n}-1)"
        reasoning = f"nth term = a × r^(n-1) = {a} × {r}^{n-1} = {answer}."

    assert_valid_answer(answer, "sequences")
    return {
        "domain": "sequences",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
