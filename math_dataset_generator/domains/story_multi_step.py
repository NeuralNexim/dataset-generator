import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
OBJECTS = ["apples", "oranges", "books", "pencils", "marbles", "coins"]


def generate_story_multi_step_sample(difficulty: str = "medium"):
    """
    Generates a multi-step story problem (2–3 steps).
    Example:
        Alice had 5 apples. She bought 3 more. Then she gave 2 away.
        How many apples does she have now?
    """
    if difficulty == "easy":
        a_range = (3, 8)
        b_range = (2, 5)
        c_range = (1, 3)
    elif difficulty == "hard":
        a_range = (10, 50)
        b_range = (5, 20)
        c_range = (3, 15)
    elif difficulty == "olympiad":
        a_range = (50, 500)
        b_range = (20, 200)
        c_range = (10, 100)
    else:  # medium
        a_range = (3, 12)
        b_range = (2, 8)
        c_range = (1, 6)

    name = random.choice(NAMES)
    obj = random.choice(OBJECTS)

    # Step values
    a = random.randint(*a_range)
    b = random.randint(*b_range)
    c = random.randint(*c_range)

    # Choose a pattern
    pattern = random.choice(["add_add", "add_sub", "sub_add"])

    if pattern == "add_add":
        question = get_template("story_multi", "add_add", difficulty).format(
            name=name, a=a, b=b, c=c, obj=obj
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
        question = get_template("story_multi", "add_sub", difficulty).format(
            name=name, a=a, b=b, c=c, obj=obj
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
        question = get_template("story_multi", "sub_add", difficulty).format(
            name=name, a=a2, b=b2, c=c, obj=obj
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
        "difficulty": difficulty,
    }
