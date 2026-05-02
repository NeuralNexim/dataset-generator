from math_dataset_generator.utils.config import CONFIG

# ---------------------------------------------------------------------------
# Tamil lookup tables not held in CONFIG (sandhi / combination forms)
# ---------------------------------------------------------------------------

_TA_TEENS: dict[int, str] = {
    11: "பதினொன்று",
    12: "பன்னிரண்டு",
    13: "பதிமூன்று",
    14: "பதினான்கு",
    15: "பதினைந்து",
    16: "பதினாறு",
    17: "பதினேழு",
    18: "பதினெட்டு",
    19: "பத்தொன்பது",
}

# Combination form of the tens digit when a unit follows it (e.g. 21 = இருபத்தி ஒன்று)
_TA_TENS_COMBO: dict[int, str] = {
    20: "இருபத்தி",
    30: "முப்பத்தி",
    40: "நாற்பத்தி",
    50: "ஐம்பத்தி",
    60: "அறுபத்தி",
    70: "எழுபத்தி",
    80: "எண்பத்தி",
    90: "தொண்ணூத்தி",
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def number_to_words(n: int, lang: str = "en") -> str:
    """Convert an integer to its word representation."""
    cfg = CONFIG["languages"][lang]
    if n > cfg["max_number"]:
        raise ValueError(f"{lang} supports up to {cfg['max_number']}, got {n}")

    if lang == "en":
        return _number_to_words_en(n, cfg)
    if lang == "ta":
        return _number_to_words_ta(n, cfg)
    raise ValueError(f"Unsupported language: {lang}")


def words_to_number(text: str, lang: str = "en") -> int:
    """Convert a word representation back to an integer."""
    if lang == "en":
        return _words_to_number_en(text)
    if lang == "ta":
        return _words_to_number_ta(text)
    raise ValueError(f"Unsupported language: {lang}")


# ---------------------------------------------------------------------------
# English implementation
# ---------------------------------------------------------------------------


def _number_to_words_en(n: int, cfg: dict) -> str:
    d = cfg["dictionary"]
    units = d["units"]
    teens = d["teens"]
    tens = d["tens"]
    supports_and = cfg.get("supports_and", False)

    if n == 0:
        return units[0]

    parts: list[str] = []

    if n >= 1_000_000:
        parts.append(_number_to_words_en(n // 1_000_000, cfg) + " million")
        n %= 1_000_000

    if n >= 1_000:
        parts.append(_number_to_words_en(n // 1_000, cfg) + " thousand")
        n %= 1_000

    if n >= 100:
        parts.append(units[n // 100] + " hundred")
        n %= 100
        if n > 0 and supports_and:
            parts.append("and")

    if n >= 20:
        ten, unit = (n // 10) * 10, n % 10
        parts.append(tens[ten] + (" " + units[unit] if unit else ""))
    elif n >= 10:
        parts.append(teens[n])
    elif n > 0:
        parts.append(units[n])

    return " ".join(parts)


def _words_to_number_en(text: str) -> int:
    d = CONFIG["languages"]["en"]["dictionary"]

    word_val: dict[str, int] = {}
    for k, v in d["units"].items():
        word_val[v] = k
    for k, v in d["teens"].items():
        word_val[v] = k
    for k, v in d["tens"].items():
        word_val[v] = k

    tokens = [
        t
        for t in text.lower().replace("-", " ").replace(",", " ").split()
        if t != "and"
    ]

    result = 0
    current = 0

    for token in tokens:
        if token == "hundred":
            current *= 100
        elif token == "thousand":
            current *= 1_000
            result += current
            current = 0
        elif token == "million":
            current *= 1_000_000
            result += current
            current = 0
        else:
            current += word_val.get(token, 0)

    result += current
    return result


# ---------------------------------------------------------------------------
# Tamil implementation
# ---------------------------------------------------------------------------


def _number_to_words_ta(n: int, cfg: dict) -> str:
    d = cfg["dictionary"]
    units = d["units"]
    tens = d["tens"]
    scales = d["scales"]

    if n == 0:
        return units[0]

    parts: list[str] = []

    if n >= 100_000:
        parts.append(_number_to_words_ta(n // 100_000, cfg) + " " + scales[100_000])
        n %= 100_000

    if n >= 1_000:
        parts.append(_number_to_words_ta(n // 1_000, cfg) + " " + scales[1_000])
        n %= 1_000

    if n >= 100:
        parts.append(units[n // 100] + " " + scales[100])
        n %= 100

    if 11 <= n <= 19:
        parts.append(_TA_TEENS[n])
    elif n >= 20:
        ten, unit = (n // 10) * 10, n % 10
        if unit:
            parts.append(_TA_TENS_COMBO[ten] + " " + units[unit])
        else:
            parts.append(tens[ten])
    elif n == 10:
        parts.append(tens[10])
    elif n > 0:
        parts.append(units[n])

    return " ".join(parts)


def _words_to_number_ta(text: str) -> int:
    d = CONFIG["languages"]["ta"]["dictionary"]

    word_val: dict[str, int] = {}
    for k, v in d["units"].items():
        word_val[v] = k
    for k, v in d["tens"].items():
        word_val[v] = k
    for k, v in _TA_TEENS.items():
        word_val[v] = k
    for k, v in _TA_TENS_COMBO.items():
        word_val[v] = k

    scale_val: dict[str, int] = {v: k for k, v in d["scales"].items()}

    tokens = text.strip().split()
    result = 0
    current = 0

    for token in tokens:
        if token in scale_val:
            scale = scale_val[token]
            if scale == 100:
                current *= 100
            else:
                current *= scale
                result += current
                current = 0
        else:
            current += word_val.get(token, 0)

    result += current
    return result
