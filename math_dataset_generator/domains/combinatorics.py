"""
Combinatorics Domain
Generates problems involving permutations, combinations, and basic counting.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer


def _perm(n: int, r: int) -> int:
    return math.perm(n, r)


def _comb(n: int, r: int) -> int:
    return math.comb(n, r)


def generate_combinatorics_sample() -> dict:
    pattern = random.choice(["permutation", "combination", "counting"])

    if pattern == "permutation":
        n = random.randint(4, 9)
        r = random.randint(2, min(3, n))
        answer = _perm(n, r)
        question = (
            f"How many ways can {r} items be arranged from a set of {n} distinct items "
            f"(order matters)?"
        )
        expression = f"P({n},{r})"
        reasoning = f"P({n},{r}) = {n}! / ({n}-{r})! = {answer}."

    elif pattern == "combination":
        n = random.randint(4, 10)
        r = random.randint(2, min(4, n))
        answer = _comb(n, r)
        question = (
            f"How many ways can {r} items be chosen from a set of {n} distinct items "
            f"(order does not matter)?"
        )
        expression = f"C({n},{r})"
        reasoning = f"C({n},{r}) = {n}! / ({r}! × ({n}-{r})!) = {answer}."

    else:  # counting — multiplication principle
        choices = [random.randint(2, 6) for _ in range(2)]
        answer = choices[0] * choices[1]
        question = (
            f"There are {choices[0]} choices for the first item and {choices[1]} choices "
            f"for the second item. How many combinations are there in total?"
        )
        expression = f"{choices[0]} * {choices[1]}"
        reasoning = (
            f"By the multiplication principle: {choices[0]} × {choices[1]} = {answer}."
        )

    assert_valid_answer(answer, "combinatorics")
    return {
        "domain": "combinatorics",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
