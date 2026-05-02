import random


def generate_proportional_sample():
    """
    Generates simple proportional reasoning problems.
    """

    a = random.randint(2, 8)
    b = random.randint(2, 8)
    scale = random.randint(2, 5)

    question = f"If {a} apples cost {b} dollars, how much do {a * scale} apples cost?"
    expression = f"{b} * {scale}"
    answer = b * scale
    reasoning = f"Cost scales proportionally: {b} * {scale} = {answer}"

    return {
        "domain": "proportional",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
