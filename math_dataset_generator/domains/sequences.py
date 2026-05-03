"""
Sequences & Series Domain
Arithmetic sequences (nth term, sum), geometric sequences (nth term).
"""

import random

from math_dataset_generator.validation import assert_valid_answer


def generate_sequences_sample() -> dict:
    pattern = random.choice(["arith_nth", "arith_sum", "geo_nth"])

    if pattern == "arith_nth":
        a = random.randint(1, 10)  # first term
        d = random.randint(1, 10)  # common difference
        n = random.randint(5, 15)  # term index
        answer = a + (n - 1) * d
        question = (
            f"An arithmetic sequence has first term {a} and common difference {d}. "
            f"What is the {n}th term?"
        )
        expression = f"{a} + ({n} - 1) * {d}"
        reasoning = (
            f"nth term = a + (n-1)d = {a} + ({n}-1) × {d} = {a} + {(n-1)*d} = {answer}."
        )

    elif pattern == "arith_sum":
        a = random.randint(1, 10)
        d = random.randint(1, 8)
        n = random.randint(4, 12)
        answer = n * (2 * a + (n - 1) * d) // 2
        question = (
            f"Find the sum of the first {n} terms of an arithmetic sequence with "
            f"first term {a} and common difference {d}."
        )
        expression = f"{n} * (2*{a} + ({n}-1)*{d}) / 2"
        reasoning = f"S = n/2 × (2a + (n-1)d) = {n}/2 × ({2*a} + {(n-1)*d}) = {answer}."

    else:  # geo_nth
        a = random.randint(1, 5)
        r = random.randint(2, 4)
        n = random.randint(3, 7)
        answer = a * (r ** (n - 1))
        question = (
            f"A geometric sequence has first term {a} and common ratio {r}. "
            f"What is the {n}th term?"
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
    }
