import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
OBJECTS = ["apples", "oranges", "books", "pencils", "marbles", "coins"]


def generate_story_single_step_sample(difficulty: str = "medium"):
    """
    Generates a simple single-step story problem.
    Example:
        Alice had 5 apples. She bought 3 more. How many apples does she have now?
    """
    if difficulty == "easy":
        lo, hi = 2, 8
    elif difficulty == "hard":
        lo, hi = 5, 50
    elif difficulty == "olympiad":
        lo, hi = 50, 500
    else:  # medium
        lo, hi = 2, 12

    name = random.choice(NAMES)
    obj = random.choice(OBJECTS)

    a = random.randint(lo, hi)
    b = random.randint(lo, hi)

    op = random.choice(["add", "sub", "mul"])

    if op == "add":
        question = get_template("story_single", "add", difficulty).format(
            name=name, a=a, b=b, obj=obj
        )
        expression = f"{a} + {b}"
        answer = a + b
        reasoning = f"{a} + {b} = {answer}"

    elif op == "sub":
        # ensure non-negative
        a, b = max(a, b), min(a, b)
        question = get_template("story_single", "sub", difficulty).format(
            name=name, a=a, b=b, obj=obj
        )
        expression = f"{a} - {b}"
        answer = a - b
        reasoning = f"{a} - {b} = {answer}"

    else:  # mul
        question = get_template("story_single", "mul", difficulty).format(
            name=name, a=a, b=b, obj=obj
        )
        expression = f"{a} * {b}"
        answer = a * b
        reasoning = f"{a} * {b} = {answer}"

    assert_valid_answer(answer, "story_single")
    return {
        "domain": "story_single",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
