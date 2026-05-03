import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_arithmetic_sample(difficulty: str = "medium"):
    """
    Generates a simple arithmetic problem: +, -, *, or //.
    Ensures non-negative subtraction and integer division.
    """
    if difficulty == "easy":
        lo, hi = 2, 10
    elif difficulty == "hard":
        lo, hi = 10, 100
    elif difficulty == "olympiad":
        lo, hi = 100, 1000
    else:  # medium
        lo, hi = 2, 20

    op = random.choice(["add", "sub", "mul", "div"])

    a = random.randint(lo, hi)
    b = random.randint(lo, hi)

    if op == "add":
        question = get_template("arithmetic", "add", difficulty).format(a=a, b=b)
        expression = f"{a} + {b}"
        answer = a + b
        reasoning = f"{a} + {b} = {answer}"

    elif op == "sub":
        # ensure non-negative
        a2, b2 = max(a, b), min(a, b)
        question = get_template("arithmetic", "sub", difficulty).format(a=a2, b=b2)
        expression = f"{a2} - {b2}"
        answer = a2 - b2
        reasoning = f"{a2} - {b2} = {answer}"

    elif op == "mul":
        question = get_template("arithmetic", "mul", difficulty).format(a=a, b=b)
        expression = f"{a} * {b}"
        answer = a * b
        reasoning = f"{a} * {b} = {answer}"

    else:  # div
        # ensure clean division
        answer = a
        result = a * b
        question = get_template("arithmetic", "div", difficulty).format(
            result=result, b=b
        )
        expression = f"{result} / {b}"
        reasoning = f"{result} / {b} = {answer}"

    assert_valid_answer(answer, "arithmetic")
    return {
        "domain": "arithmetic",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
