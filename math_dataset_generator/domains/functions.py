import random


def generate_functions_sample():
    """
    Generates simple function-evaluation problems.
    Example:
        f(x) = 3x + 2
        x = 4
        f(4) = 14
    """

    # Random linear function
    a = random.randint(1, 9)
    b = random.randint(0, 9)
    x = random.randint(1, 10)

    expression = f"{a}x + {b}"
    answer = a * x + b

    return {
        "domain": "functions",
        "input": f"If f(x) = {expression}, what is f({x})?",
        "expression": f"{a}*{x} + {b}",
        "reasoning": f"f({x}) = {a}*{x} + {b} = {answer}",
        "answer": answer,
    }
