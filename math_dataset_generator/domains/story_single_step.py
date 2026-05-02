import random

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
OBJECTS = ["apples", "oranges", "books", "pencils", "marbles", "coins"]


def generate_story_single_step_sample():
    """
    Generates a simple single-step story problem.
    Example:
        Alice had 5 apples. She bought 3 more. How many apples does she have now?
    """

    name = random.choice(NAMES)
    obj = random.choice(OBJECTS)

    a = random.randint(2, 12)
    b = random.randint(2, 12)

    op = random.choice(["add", "sub", "mul"])

    if op == "add":
        question = f"{name} had {a} {obj}. {name} got {b} more. How many {obj} does {name} have now?"
        expression = f"{a} + {b}"
        answer = a + b
        reasoning = f"{a} + {b} = {answer}"

    elif op == "sub":
        # ensure non-negative
        a, b = max(a, b), min(a, b)
        question = f"{name} had {a} {obj}. {name} gave away {b}. How many {obj} does {name} have now?"
        expression = f"{a} - {b}"
        answer = a - b
        reasoning = f"{a} - {b} = {answer}"

    else:  # mul
        question = f"{name} has {a} bags with {b} {obj} in each. How many {obj} does {name} have in total?"
        expression = f"{a} * {b}"
        answer = a * b
        reasoning = f"{a} * {b} = {answer}"

    return {
        "domain": "story_single",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
