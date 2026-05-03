import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_units_rates_sample(difficulty: str = "medium"):
    """
    Generates simple unit-rate or speed-time-distance problems.
    """
    if difficulty == "easy":
        speed_range = (10, 40)
        time_range = (1, 3)
        rate_range = (2, 8)
        hours_range = (1, 4)
        meters_range = (100, 500)
    elif difficulty == "hard":
        speed_range = (50, 200)
        time_range = (2, 10)
        rate_range = (10, 50)
        hours_range = (3, 12)
        meters_range = (500, 5000)
    elif difficulty == "olympiad":
        speed_range = (200, 500)
        time_range = (5, 20)
        rate_range = (50, 200)
        hours_range = (8, 24)
        meters_range = (1000, 50000)
    else:  # medium
        speed_range = (20, 80)
        time_range = (1, 5)
        rate_range = (3, 12)
        hours_range = (2, 6)
        meters_range = (100, 900)

    pattern = random.choice(["speed", "rate", "conversion"])

    if pattern == "speed":
        speed = random.randint(*speed_range)
        time = random.randint(*time_range)
        distance = speed * time

        question = get_template("units_rates", "speed", difficulty).format(
            speed=speed, time=time
        )
        expression = f"{speed} * {time}"
        reasoning = f"{speed} * {time} = {distance}"
        answer = distance

    elif pattern == "rate":
        rate = random.randint(*rate_range)
        hours = random.randint(*hours_range)
        total = rate * hours

        question = get_template("units_rates", "rate", difficulty).format(
            rate=rate, hours=hours
        )
        expression = f"{rate} * {hours}"
        reasoning = f"{rate} * {hours} = {total}"
        answer = total

    else:  # conversion
        meters = random.randint(*meters_range)
        km = meters / 1000

        question = get_template("units_rates", "conversion", difficulty).format(
            meters=meters
        )
        expression = f"{meters} / 1000"
        reasoning = f"{meters} / 1000 = {km}"
        answer = km

    assert_valid_answer(answer, "units_rates")
    return {
        "domain": "units_rates",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
