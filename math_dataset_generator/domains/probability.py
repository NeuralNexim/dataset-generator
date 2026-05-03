"""
Probability Domain
Generates simple probability problems: coins, dice, coloured balls.
Answers are rational fractions expressed as floats (0 ≤ p ≤ 1).
"""

import random
from fractions import Fraction

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_probability_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["coin", "dice", "balls"])

    if difficulty == "easy":
        ball_lo, ball_hi = 1, 4
    elif difficulty == "hard":
        ball_lo, ball_hi = 5, 20
    elif difficulty == "olympiad":
        ball_lo, ball_hi = 10, 50
    else:  # medium
        ball_lo, ball_hi = 1, 8

    if pattern == "coin":
        flips = random.randint(1, 1)  # single flip keeps answer clean
        side = random.choice(["heads", "tails"])
        prob = Fraction(1, 2)
        question = get_template("probability", "coin", difficulty).format(side=side)
        expression = "1 / 2"
        reasoning = f"There is 1 favourable outcome ({side}) out of 2 equally likely outcomes. P = 1/2."

    elif pattern == "dice":
        target = random.randint(1, 6)
        prob = Fraction(1, 6)
        question = get_template("probability", "dice", difficulty).format(target=target)
        expression = "1 / 6"
        reasoning = f"There is 1 favourable outcome ({target}) out of 6 equally likely outcomes. P = 1/6."

    else:  # balls
        red = random.randint(ball_lo, ball_hi)
        blue = random.randint(ball_lo, ball_hi)
        total = red + blue
        colour = random.choice(["red", "blue"])
        favourable = red if colour == "red" else blue
        prob = Fraction(favourable, total)
        question = get_template("probability", "balls", difficulty).format(
            red=red, blue=blue, total=total, colour=colour, favourable=favourable
        )
        expression = f"{favourable} / {total}"
        reasoning = (
            f"There are {favourable} {colour} balls out of {total} total. "
            f"P = {favourable}/{total}."
        )

    answer = float(prob)
    assert_valid_answer(answer, "probability")
    return {
        "domain": "probability",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
