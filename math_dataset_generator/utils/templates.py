"""
Reusable templates for all domains.
Keeps domain modules clean and consistent.
"""

import random
from typing import Dict, Any
from math_dataset_generator.exceptions import TemplateError

# ---------------------------------------------------------
# Template rendering helper
# ---------------------------------------------------------


def render_template(template: str, **kwargs) -> str:
    """
    Render a template with placeholders like {a}, {b}, {name}.
    Raises TemplateError if a placeholder is missing.
    """
    try:
        return template.format(**kwargs)
    except KeyError as exc:
        raise TemplateError(
            f"Missing placeholder {exc} in template: {template!r}"
        ) from exc


# ---------------------------------------------------------
# Names, units, objects
# ---------------------------------------------------------

NAMES = [
    "John",
    "Sarah",
    "Aisha",
    "Ravi",
    "Maya",
    "Daniel",
    "Priya",
    "Liam",
    "Emma",
    "Noah",
    "Olivia",
]

OBJECTS = [
    "apples",
    "oranges",
    "books",
    "pencils",
    "marbles",
    "stickers",
    "coins",
    "cups",
    "blocks",
]

UNITS = ["km", "m", "cm", "kg", "g", "hours", "minutes", "liters"]


# ---------------------------------------------------------
# Story problem templates
# ---------------------------------------------------------

STORY_SINGLE_STEP = [
    "{name} has {a} {obj} and buys {b} more. How many {obj} now?",
    "A box contains {a} {obj}. {b} more are added. How many now?",
    "There are {a} birds on a tree. {b} fly away. How many remain?",
]

STORY_MULTI_STEP = [
    "{name} buys {a} {obj}. They give {b} to a friend, then buy {c} more. "
    "How many {obj} do they have now?",
    "{name} walks {a} km in the morning and {b} km in the afternoon. "
    "Next day they walk {c} km. What is the total distance?",
]


# ---------------------------------------------------------
# Units & rates templates
# ---------------------------------------------------------

UNITS_RATES = [
    "A car travels at {speed} km/h for {time} hours. How far does it go?",
    "{name} runs at {speed} m/s for {time} seconds. What distance do they cover?",
    "Water flows at {rate} liters per minute for {time} minutes. How much water flows?",
]


# ---------------------------------------------------------
# Proportional reasoning templates
# ---------------------------------------------------------

PROPORTIONAL = [
    "If {a} items cost {b} dollars, how much do {a2} items cost?",
    "A recipe uses {a} cups of flour for {b} cookies. How much flour for {a2} cookies?",
]


# ---------------------------------------------------------
# Geometry templates
# ---------------------------------------------------------

GEOMETRY = [
    "Rectangle with width {w} and height {h}. Find the area.",
    "Triangle with base {b} and height {h}. Find the area.",
]


# ---------------------------------------------------------
# Algebra templates
# ---------------------------------------------------------

ALGEBRA = [
    "Solve for x: {a}x + {b} = {c}",
    "Find x: {a}x - {b} = {c}",
]


# ---------------------------------------------------------
# Mixed domain templates
# ---------------------------------------------------------

MIXED = STORY_SINGLE_STEP + STORY_MULTI_STEP + UNITS_RATES + PROPORTIONAL + GEOMETRY


# ---------------------------------------------------------
# Template selection helpers
# ---------------------------------------------------------


def choose_name() -> str:
    return random.choice(NAMES)


def choose_object() -> str:
    return random.choice(OBJECTS)


def choose_unit() -> str:
    return random.choice(UNITS)


def choose_template(category: str) -> str:
    """
    Select a template from a category.
    """
    mapping = {
        "story_single": STORY_SINGLE_STEP,
        "story_multi": STORY_MULTI_STEP,
        "units_rates": UNITS_RATES,
        "proportional": PROPORTIONAL,
        "geometry": GEOMETRY,
        "algebra": ALGEBRA,
        "mixed": MIXED,
    }

    if category not in mapping:
        raise ValueError(f"Unknown template category: {category}")

    return random.choice(mapping[category])
