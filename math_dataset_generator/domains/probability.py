"""
Probability Domain
Generates simple probability problems: coins, dice, coloured balls.
Answers are rational fractions expressed as floats (0 ≤ p ≤ 1).
"""

import random
from fractions import Fraction

from math_dataset_generator.validation import assert_valid_answer


def generate_probability_sample() -> dict:
    pattern = random.choice(["coin", "dice", "balls"])

    if pattern == "coin":
        flips = random.randint(1, 1)  # single flip keeps answer clean
        side = random.choice(["heads", "tails"])
        prob = Fraction(1, 2)
        question = f"A fair coin is flipped. What is the probability of getting {side}?"
        expression = "1 / 2"
        reasoning = f"There is 1 favourable outcome ({side}) out of 2 equally likely outcomes. P = 1/2."

    elif pattern == "dice":
        target = random.randint(1, 6)
        prob = Fraction(1, 6)
        question = f"A fair six-sided die is rolled. What is the probability of rolling a {target}?"
        expression = "1 / 6"
        reasoning = f"There is 1 favourable outcome ({target}) out of 6 equally likely outcomes. P = 1/6."

    else:  # balls
        red = random.randint(1, 8)
        blue = random.randint(1, 8)
        total = red + blue
        colour = random.choice(["red", "blue"])
        favourable = red if colour == "red" else blue
        prob = Fraction(favourable, total)
        question = (
            f"A bag contains {red} red balls and {blue} blue balls. "
            f"One ball is drawn at random. What is the probability it is {colour}?"
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
    }
