import random
from math_dataset_generator.validation import assert_valid_answer

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
OBJECTS = ["apples", "oranges", "books", "pencils", "marbles", "coins"]


def generate_story_multi_step_sample():
    """
    Generates a multi-step story problem (2–3 steps).
    Example:
        Alice had 5 apples. She bought 3 more. Then she gave 2 away.
        How many apples does she have now?
    """

    name = random.choice(NAMES)
    obj = random.choice(OBJECTS)

    # Step values
    a = random.randint(3, 12)
    b = random.randint(2, 8)
    c = random.randint(1, 6)

    # Choose a pattern
    pattern = random.choice(["add_add", "add_sub", "sub_add"])

    if pattern == "add_add":
        question = (
            f"{name} had {a} {obj}. "
            f"{name} got {b} more. "
            f"Then {name} found {c} more. "
            f"How many {obj} does {name} have now?"
        )
        expression = f"{a} + {b} + {c}"
        step1 = a + b
        answer = step1 + c
        reasoning = (
            f"Step 1: {a} + {b} = {step1}. " f"Step 2: {step1} + {c} = {answer}."
        )

    elif pattern == "add_sub":
        step1 = a + b
        c = max(1, min(c, step1))  # ensure 1 <= c <= step1 so answer >= 0
        question = (
            f"{name} had {a} {obj}. "
            f"{name} got {b} more. "
            f"Then {name} gave away {c}. "
            f"How many {obj} does {name} have now?"
        )
        expression = f"{a} + {b} - {c}"
        answer = step1 - c
        reasoning = (
            f"Step 1: {a} + {b} = {step1}. " f"Step 2: {step1} - {c} = {answer}."
        )

    else:  # sub_add
        # ensure non-negative
        a2 = max(a, b)
        b2 = min(a, b)
        question = (
            f"{name} had {a2} {obj}. "
            f"{name} gave away {b2}. "
            f"Then {name} got {c} more. "
            f"How many {obj} does {name} have now?"
        )
        expression = f"{a2} - {b2} + {c}"
        step1 = a2 - b2
        answer = step1 + c
        reasoning = (
            f"Step 1: {a2} - {b2} = {step1}. " f"Step 2: {step1} + {c} = {answer}."
        )

    assert_valid_answer(answer, "story_multi")
    return {
        "domain": "story_multi",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
