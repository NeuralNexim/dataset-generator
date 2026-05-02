import random
from typing import Literal

NoiseLevel = Literal["light", "medium", "heavy"]


def apply_noise(text: str, level: NoiseLevel) -> str:
    """
    Apply controlled noise to text for robustness training.
    """

    if level == "light":
        return _typo_noise(text, probability=0.03)

    if level == "medium":
        text = _typo_noise(text, probability=0.05)
        text = _punctuation_noise(text, probability=0.05)
        return text

    if level == "heavy":
        text = _typo_noise(text, probability=0.08)
        text = _punctuation_noise(text, probability=0.10)
        text = _insert_filler(text, probability=0.10)
        return text

    return text


def _typo_noise(text: str, probability: float) -> str:
    chars = list(text)
    for i in range(len(chars)):
        if random.random() < probability:
            chars[i] = random.choice("abcdefghijklmnopqrstuvwxyz")
    return "".join(chars)


def _punctuation_noise(text: str, probability: float) -> str:
    punct = ["!", "?", "...", "—", ",,", "!!"]
    words = text.split()
    for i in range(len(words)):
        if random.random() < probability:
            words[i] += random.choice(punct)
    return " ".join(words)


def _insert_filler(text: str, probability: float) -> str:
    fillers = ["uh", "erm", "like", "you know", "hmm"]
    words = text.split()
    out = []
    for w in words:
        out.append(w)
        if random.random() < probability:
            out.append(random.choice(fillers))
    return " ".join(out)
