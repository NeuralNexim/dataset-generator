"""
Combinatorics Domain
Generates problems involving permutations, combinations, and basic counting.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def _perm(n: int, r: int) -> int:
    return math.perm(n, r)


def _comb(n: int, r: int) -> int:
    return math.comb(n, r)


def generate_combinatorics_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["permutation", "combination", "counting"])

    if difficulty == "easy":
        perm_n_range = (4, 6)
        comb_n_range = (4, 7)
        count_range = (2, 4)
    elif difficulty == "hard":
        perm_n_range = (8, 15)
        comb_n_range = (8, 15)
        count_range = (4, 9)
    elif difficulty == "olympiad":
        perm_n_range = (12, 20)
        comb_n_range = (12, 20)
        count_range = (6, 12)
    else:  # medium
        perm_n_range = (4, 9)
        comb_n_range = (4, 10)
        count_range = (2, 6)

    if pattern == "permutation":
        n = random.randint(*perm_n_range)
        r = random.randint(2, min(3, n))
        answer = _perm(n, r)
        question = get_template("combinatorics", "permutation", difficulty).format(
            n=n, r=r
        )
        expression = f"P({n},{r})"
        reasoning = f"P({n},{r}) = {n}! / ({n}-{r})! = {answer}."

    elif pattern == "combination":
        n = random.randint(*comb_n_range)
        r = random.randint(2, min(4, n))
        answer = _comb(n, r)
        question = get_template("combinatorics", "combination", difficulty).format(
            n=n, r=r
        )
        expression = f"C({n},{r})"
        reasoning = f"C({n},{r}) = {n}! / ({r}! × ({n}-{r})!) = {answer}."

    else:  # counting — multiplication principle
        choices = [random.randint(*count_range) for _ in range(2)]
        answer = choices[0] * choices[1]
        question = get_template("combinatorics", "counting", difficulty).format(
            c0=choices[0], c1=choices[1]
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
        "difficulty": difficulty,
    }
