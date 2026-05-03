import random
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_proportional_sample(difficulty: str = "medium"):
    """
    Generates simple proportional reasoning problems.
    """
    if difficulty == "easy":
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        scale = random.randint(2, 3)
    elif difficulty == "hard":
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        scale = random.randint(3, 10)
    elif difficulty == "olympiad":
        a = random.randint(10, 50)
        b = random.randint(50, 200)
        scale = random.randint(10, 50)
    else:  # medium
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        scale = random.randint(2, 5)

    question = get_template("proportional", "_default", difficulty).format(
        a=a, b=b, a2=a * scale
    )
    expression = f"{b} * {scale}"
    answer = b * scale
    reasoning = f"Cost scales proportionally: {b} * {scale} = {answer}"

    assert_valid_answer(answer, "proportional")
    return {
        "domain": "proportional",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
