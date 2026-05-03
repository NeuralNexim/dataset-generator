"""
Word Numbers Domain
Converts numbers to words and requires the model to convert back.
"""

import random
from typing import Dict, Any
from math_dataset_generator.utils.word_to_number import number_to_words, words_to_number
from math_dataset_generator.utils.config import MAX_WORD_NUMBER
from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_word_numbers_sample(difficulty: str = "medium") -> Dict[str, Any]:
    if difficulty == "easy":
        n = random.randint(0, 100)
    elif difficulty == "medium":
        n = random.randint(100, 9999)
    elif difficulty in ("hard", "olympiad"):
        n = random.randint(10000, MAX_WORD_NUMBER)
    else:
        return generate_word_numbers_sample(
            random.choice(["easy", "medium", "hard", "olympiad"])
        )

    words = number_to_words(n)
    answer = words_to_number(words)
    question = get_template("word_numbers", "_default", difficulty).format(words=words)

    assert_valid_answer(answer, "word_numbers")
    return {
        "domain": "word_numbers",
        "input": question,
        "expression": words,
        "reasoning": f"{words} -> {answer}",
        "answer": answer,
        "difficulty": difficulty,
    }
