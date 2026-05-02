from math_dataset_generator.utils.word_to_number import number_to_words, words_to_number
from math_dataset_generator.utils.config import MAX_WORD_NUMBER

def test_roundtrip_small():
    for n in range(0, min(1000, MAX_WORD_NUMBER + 1)):
        words = number_to_words(n)
        back = words_to_number(words)
        assert back == n

def test_specific_cases():
    cases = {
        "zero": 0,
        "twenty one": 21,
        "one hundred and five": 105,
        "nine thousand nine hundred ninety nine": 9999,
    }
    for text, expected in cases.items():
        assert words_to_number(text) == expected
