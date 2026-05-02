import random


def generate_arithmetic_sample():
    """
    Generates a simple arithmetic problem: +, -, *, or //.
    Ensures non-negative subtraction and integer division.
    """

    op = random.choice(["add", "sub", "mul", "div"])

    a = random.randint(2, 20)
    b = random.randint(2, 20)

    if op == "add":
        question = f"What is {a} + {b}?"
        expression = f"{a} + {b}"
        answer = a + b
        reasoning = f"{a} + {b} = {answer}"

    elif op == "sub":
        # ensure non-negative
        a2, b2 = max(a, b), min(a, b)
        question = f"What is {a2} - {b2}?"
        expression = f"{a2} - {b2}"
        answer = a2 - b2
        reasoning = f"{a2} - {b2} = {answer}"

    elif op == "mul":
        question = f"What is {a} × {b}?"
        expression = f"{a} * {b}"
        answer = a * b
        reasoning = f"{a} * {b} = {answer}"

    else:  # div
        # ensure clean division
        answer = a
        result = a * b
        question = f"What is {result} ÷ {b}?"
        expression = f"{result} / {b}"
        reasoning = f"{result} / {b} = {answer}"

    return {
        "domain": "arithmetic",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
