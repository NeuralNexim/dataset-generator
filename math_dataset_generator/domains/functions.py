import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_functions_sample(difficulty: str = "medium"):
    """
    Generates simple function-evaluation problems.
    Example:
        f(x) = 3x + 2
        x = 4
        f(4) = 14
    """
    if difficulty == "easy":
        a = random.randint(1, 5)
        b = random.randint(0, 5)
        x = random.randint(1, 5)
    elif difficulty == "hard":
        a = random.randint(5, 20)
        b = random.randint(0, 20)
        x = random.randint(5, 30)
    elif difficulty == "olympiad":
        a = random.randint(10, 50)
        b = random.randint(0, 50)
        x = random.randint(10, 100)
    else:  # medium
        a = random.randint(1, 9)
        b = random.randint(0, 9)
        x = random.randint(1, 10)

    expression = f"{a}x + {b}"
    answer = a * x + b

    question = get_template("functions", "_default", difficulty).format(
        expr=expression, x=x
    )

    assert_valid_answer(answer, "functions")
    return {
        "domain": "functions",
        "input": question,
        "expression": f"{a}*{x} + {b}",
        "reasoning": f"f({x}) = {a}*{x} + {b} = {answer}",
        "answer": answer,
        "difficulty": difficulty,
    }
