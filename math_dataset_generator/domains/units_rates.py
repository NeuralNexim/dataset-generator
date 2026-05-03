import random
from math_dataset_generator.validation import assert_valid_answer


def generate_units_rates_sample():
    """
    Generates simple unit-rate or speed-time-distance problems.
    """

    pattern = random.choice(["speed", "rate", "conversion"])

    if pattern == "speed":
        speed = random.randint(20, 80)
        time = random.randint(1, 5)
        distance = speed * time

        question = (
            f"A car travels at {speed} km/h for {time} hours. How far does it travel?"
        )
        expression = f"{speed} * {time}"
        reasoning = f"{speed} * {time} = {distance}"
        answer = distance

    elif pattern == "rate":
        rate = random.randint(3, 12)
        hours = random.randint(2, 6)
        total = rate * hours

        question = f"A machine produces {rate} items per hour. How many items in {hours} hours?"
        expression = f"{rate} * {hours}"
        reasoning = f"{rate} * {hours} = {total}"
        answer = total

    else:  # conversion
        meters = random.randint(100, 900)
        km = meters / 1000

        question = f"Convert {meters} meters to kilometers."
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
    }
