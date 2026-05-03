"""
Word Numbers Domain
Converts numbers to words and requires the model to convert back.
"""

import random
from typing import Dict, Any
from math_dataset_generator.utils.word_to_number import number_to_words, words_to_number
from math_dataset_generator.utils.config import MAX_WORD_NUMBER
from math_dataset_generator.validation import assert_valid_answer


def generate_word_numbers_sample(difficulty: str = "auto") -> Dict[str, Any]:
    if difficulty == "easy":
        n = random.randint(0, 100)
    elif difficulty == "medium":
        n = random.randint(100, 9999)
    elif difficulty == "hard":
        n = random.randint(10000, MAX_WORD_NUMBER)
    else:
        return generate_word_numbers_sample(random.choice(["easy", "medium", "hard"]))

    words = number_to_words(n)
    answer = words_to_number(words)

    assert_valid_answer(answer, "word_numbers")
    return {
        "domain": "word_numbers",
        "input": f"Convert this number in words to digits: {words}",
        "expression": words,
        "reasoning": f"{words} -> {answer}",
        "answer": answer,
    }
