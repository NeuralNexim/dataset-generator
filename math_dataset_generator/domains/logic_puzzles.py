"""
Logic Puzzles Domain
Truth/lie puzzles, age puzzles, simple deduction (text-only).
Answers are always non-negative integers.
"""

import random

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template

_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]


def generate_logic_puzzles_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["age_diff", "age_sum", "simple_deduction"])

    if difficulty == "easy":
        age_lo, age_hi = 10, 30
        diff_lo, diff_hi = 1, 8
        item_lo, item_hi = 3, 12
        give_scale = 0.4
        receive_lo, receive_hi = 1, 5
    elif difficulty == "hard":
        age_lo, age_hi = 30, 80
        diff_lo, diff_hi = 5, 30
        item_lo, item_hi = 20, 100
        give_scale = 0.6
        receive_lo, receive_hi = 5, 30
    elif difficulty == "olympiad":
        age_lo, age_hi = 50, 120
        diff_lo, diff_hi = 10, 50
        item_lo, item_hi = 100, 500
        give_scale = 0.7
        receive_lo, receive_hi = 10, 100
    else:  # medium
        age_lo, age_hi = 20, 50
        diff_lo, diff_hi = 1, 15
        item_lo, item_hi = 5, 20
        give_scale = 0.5
        receive_lo, receive_hi = 1, 10

    if pattern == "age_diff":
        names = random.sample(_NAMES, 2)
        older_age = random.randint(age_lo, age_hi)
        diff = random.randint(diff_lo, diff_hi)
        younger_age = older_age - diff
        answer = diff
        question = get_template("logic_puzzles", "age_diff", difficulty).format(
            n0=names[0], n1=names[1], a0=older_age, a1=younger_age
        )
        expression = f"{older_age} - {younger_age}"
        reasoning = f"{older_age} - {younger_age} = {answer}."

    elif pattern == "age_sum":
        names = random.sample(_NAMES, 2)
        a_age = random.randint(age_lo, age_hi)
        b_age = random.randint(age_lo, age_hi)
        answer = a_age + b_age
        question = get_template("logic_puzzles", "age_sum", difficulty).format(
            n0=names[0], n1=names[1], a0=a_age, a1=b_age
        )
        expression = f"{a_age} + {b_age}"
        reasoning = f"{a_age} + {b_age} = {answer}."

    else:  # simple_deduction
        # "X has N items, gives away K, receives M. How many does X have?"
        name = random.choice(_NAMES)
        start = random.randint(item_lo, item_hi)
        give = max(1, int(start * give_scale))
        give = random.randint(1, give)
        receive = random.randint(receive_lo, receive_hi)
        answer = start - give + receive
        question = get_template("logic_puzzles", "simple_deduction", difficulty).format(
            name=name, start=start, give=give, receive=receive
        )
        expression = f"{start} - {give} + {receive}"
        reasoning = (
            f"{start} - {give} = {start - give}; {start - give} + {receive} = {answer}."
        )

    assert_valid_answer(answer, "logic_puzzles")
    return {
        "domain": "logic_puzzles",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
