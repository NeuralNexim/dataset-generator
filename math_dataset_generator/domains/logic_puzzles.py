"""
Logic Puzzles Domain
Truth/lie puzzles, age puzzles, simple deduction (text-only).
Answers are always non-negative integers.
"""

import random

from math_dataset_generator.validation import assert_valid_answer

_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]


def generate_logic_puzzles_sample() -> dict:
    pattern = random.choice(["age_diff", "age_sum", "simple_deduction"])

    if pattern == "age_diff":
        names = random.sample(_NAMES, 2)
        older_age = random.randint(20, 50)
        diff = random.randint(1, 15)
        younger_age = older_age - diff
        answer = diff
        question = (
            f"{names[0]} is {older_age} years old and {names[1]} is {younger_age} years old. "
            f"How many years older is {names[0]} than {names[1]}?"
        )
        expression = f"{older_age} - {younger_age}"
        reasoning = f"{older_age} - {younger_age} = {answer}."

    elif pattern == "age_sum":
        names = random.sample(_NAMES, 2)
        a_age = random.randint(10, 40)
        b_age = random.randint(10, 40)
        answer = a_age + b_age
        question = (
            f"{names[0]} is {a_age} years old and {names[1]} is {b_age} years old. "
            f"What is the sum of their ages?"
        )
        expression = f"{a_age} + {b_age}"
        reasoning = f"{a_age} + {b_age} = {answer}."

    else:  # simple_deduction
        # "X has N items, gives away K, receives M. How many does X have?"
        name = random.choice(_NAMES)
        start = random.randint(5, 20)
        give = random.randint(1, start - 1)
        receive = random.randint(1, 10)
        answer = start - give + receive
        question = (
            f"{name} has {start} coins. "
            f"{name} gives away {give} and then receives {receive} more. "
            f"How many coins does {name} have now?"
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
    }
