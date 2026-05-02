import random


def generate_geometry_sample():
    """
    Generates simple geometry problems: area, perimeter.
    """

    pattern = random.choice(["rectangle_area", "rectangle_perimeter", "triangle_area"])

    if pattern == "rectangle_area":
        w = random.randint(2, 12)
        h = random.randint(2, 12)
        area = w * h

        question = f"What is the area of a rectangle with width {w} and height {h}?"
        expression = f"{w} * {h}"
        reasoning = f"{w} * {h} = {area}"
        answer = area

    elif pattern == "rectangle_perimeter":
        w = random.randint(2, 12)
        h = random.randint(2, 12)
        per = 2 * (w + h)

        question = (
            f"What is the perimeter of a rectangle with width {w} and height {h}?"
        )
        expression = f"2 * ({w} + {h})"
        reasoning = f"2 * ({w} + {h}) = {per}"
        answer = per

    else:  # triangle area
        b = random.randint(2, 12)
        h = random.randint(2, 12)
        area = 0.5 * b * h

        question = f"What is the area of a triangle with base {b} and height {h}?"
        expression = f"0.5 * {b} * {h}"
        reasoning = f"0.5 * {b} * {h} = {area}"
        answer = area

    return {
        "domain": "geometry",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
