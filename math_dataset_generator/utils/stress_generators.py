from .config import MAX_WORD_NUMBER
from .word_to_number import number_to_words, words_to_number
import random

def generate_word_number_stress_cases(count: int = 1000, seed: int | None = None):
    if seed is not None:
        random.seed(seed)

    cases = []
    for _ in range(count):
        n = random.randint(0, MAX_WORD_NUMBER)
        words = number_to_words(n)
        back = words_to_number(words)
        cases.append({
            "n": n,
            "words": words,
            "back": back,
            "ok": (n == back),
        })
    return cases
