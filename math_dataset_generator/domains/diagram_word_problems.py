"""
Diagram-based Word Problems Domain (text-only)
Problems that would typically use diagrams, described purely in text:
grid distances, shape comparisons, clock angles, coordinate distances.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_diagram_word_problems_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["grid_distance", "clock_hours", "coordinate_distance"])

    if difficulty == "easy":
        grid_offset_range = (1, 5)
        coord_offset_range = (0, 5)
    elif difficulty == "hard":
        grid_offset_range = (5, 20)
        coord_offset_range = (0, 20)
    elif difficulty == "olympiad":
        grid_offset_range = (10, 50)
        coord_offset_range = (0, 50)
    else:  # medium
        grid_offset_range = (1, 8)
        coord_offset_range = (0, 5)

    if pattern == "grid_distance":
        # Manhattan distance on a grid
        x1, y1 = random.randint(*grid_offset_range), random.randint(*grid_offset_range)
        dx = random.randint(*grid_offset_range)
        dy = random.randint(*grid_offset_range)
        x2, y2 = x1 + dx, y1 + dy
        answer = dx + dy
        question = get_template(
            "diagram_word_problems", "grid_distance", difficulty
        ).format(x1=x1, y1=y1, x2=x2, y2=y2, dx=dx, dy=dy)
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
        question = get_template(
            "diagram_word_problems", "clock_hours", difficulty
        ).format(h1=h1, h2=h2)
        expression = f"{h2} - {h1}"
        reasoning = f"{h2} - {h1} = {answer} hours."

    else:  # coordinate_distance (integer Pythagorean triples)
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        dx, dy, hyp = random.choice(triples)
        x1, y1 = random.randint(*coord_offset_range), random.randint(
            *coord_offset_range
        )
        x2, y2 = x1 + dx, y1 + dy
        answer = hyp
        question = get_template(
            "diagram_word_problems", "coordinate_distance", difficulty
        ).format(x1=x1, y1=y1, x2=x2, y2=y2, dx=dx, dy=dy)
        expression = f"sqrt(({x2}-{x1})^2 + ({y2}-{y1})^2)"
        reasoning = f"Distance = √(({dx})² + ({dy})²) = √({dx**2} + {dy**2}) = √{hyp**2} = {answer}."

    assert_valid_answer(answer, "diagram_word_problems")
    return {
        "domain": "diagram_word_problems",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
