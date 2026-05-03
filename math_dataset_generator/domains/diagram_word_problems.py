"""
Diagram-based Word Problems Domain (text-only)
Problems that would typically use diagrams, described purely in text:
grid distances, shape comparisons, clock angles, coordinate distances.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer


def generate_diagram_word_problems_sample() -> dict:
    pattern = random.choice(["grid_distance", "clock_hours", "coordinate_distance"])

    if pattern == "grid_distance":
        # Manhattan distance on a grid
        x1, y1 = random.randint(0, 8), random.randint(0, 8)
        dx = random.randint(1, 8)
        dy = random.randint(1, 8)
        x2, y2 = x1 + dx, y1 + dy
        answer = dx + dy
        question = (
            f"On a grid, point A is at ({x1}, {y1}) and point B is at ({x2}, {y2}). "
            f"Moving only horizontally or vertically, what is the shortest distance "
            f"(in grid steps) from A to B?"
        )
        expression = f"|{x2}-{x1}| + |{y2}-{y1}|"
        reasoning = (
            f"Horizontal steps: |{x2}-{x1}| = {dx}. "
            f"Vertical steps: |{y2}-{y1}| = {dy}. "
            f"Total = {dx} + {dy} = {answer}."
        )

    elif pattern == "clock_hours":
        # How many hours between two clock positions (0–12 range)
        h1 = random.randint(1, 11)
        gap = random.randint(1, 12 - h1)
        h2 = h1 + gap
        answer = gap
        question = (
            f"A clock shows {h1}:00. How many hours later will it show {h2}:00?"
        )
        expression = f"{h2} - {h1}"
        reasoning = f"{h2} - {h1} = {answer} hours."

    else:  # coordinate_distance (integer Pythagorean triples)
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        dx, dy, hyp = random.choice(triples)
        x1, y1 = random.randint(0, 5), random.randint(0, 5)
        x2, y2 = x1 + dx, y1 + dy
        answer = hyp
        question = (
            f"Point A is at ({x1}, {y1}) and point B is at ({x2}, {y2}). "
            f"What is the straight-line (Euclidean) distance between A and B?"
        )
        expression = f"sqrt(({x2}-{x1})^2 + ({y2}-{y1})^2)"
        reasoning = (
            f"Distance = √(({dx})² + ({dy})²) = √({dx**2} + {dy**2}) = √{hyp**2} = {answer}."
        )

    assert_valid_answer(answer, "diagram_word_problems")
    return {
        "domain": "diagram_word_problems",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
