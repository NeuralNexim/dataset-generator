import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_geometry_sample(difficulty: str = "medium"):
    """
    Generates simple geometry problems: area, perimeter.
    """
    if difficulty == "easy":
        lo, hi = 2, 8
    elif difficulty == "hard":
        lo, hi = 5, 30
    elif difficulty == "olympiad":
        lo, hi = 20, 100
    else:  # medium
        lo, hi = 2, 12

    pattern = random.choice(["rectangle_area", "rectangle_perimeter", "triangle_area"])

    if pattern == "rectangle_area":
        w = random.randint(lo, hi)
        h = random.randint(lo, hi)
        area = w * h

        question = get_template("geometry", "rectangle_area", difficulty).format(
            w=w, h=h
        )
        expression = f"{w} * {h}"
        reasoning = f"{w} * {h} = {area}"
        answer = area

    elif pattern == "rectangle_perimeter":
        w = random.randint(lo, hi)
        h = random.randint(lo, hi)
        per = 2 * (w + h)

        question = get_template("geometry", "rectangle_perimeter", difficulty).format(
            w=w, h=h
        )
        expression = f"2 * ({w} + {h})"
        reasoning = f"2 * ({w} + {h}) = {per}"
        answer = per

    else:  # triangle area
        b = random.randint(lo, hi)
        h = random.randint(lo, hi)
        area = 0.5 * b * h

        question = get_template("geometry", "triangle_area", difficulty).format(
            b=b, h=h
        )
        expression = f"0.5 * {b} * {h}"
        reasoning = f"0.5 * {b} * {h} = {area}"
        answer = area

    assert_valid_answer(answer, "geometry")
    return {
        "domain": "geometry",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
