"""
Global configuration for multilingual number systems.
Default languages: English + Tamil.
"""

# Upper bound for random number generation in the word_numbers domain.
# Kept at 999_999 so it stays within both EN (999_999_999) and TA (999_999) limits.
MAX_WORD_NUMBER = 999_999

CONFIG = {
    "default_languages": ["en", "ta"],
    "languages": {
        "en": {
            "max_number": 999_999_999,
            "supports_hyphens": True,
            "supports_and": True,
            "dictionary": {
                "units": {
                    0: "zero",
                    1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                    5: "five",
                    6: "six",
                    7: "seven",
                    8: "eight",
                    9: "nine",
                },
                "teens": {
                    10: "ten",
                    11: "eleven",
                    12: "twelve",
                    13: "thirteen",
                    14: "fourteen",
                    15: "fifteen",
                    16: "sixteen",
                    17: "seventeen",
                    18: "eighteen",
                    19: "nineteen",
                },
                "tens": {
                    20: "twenty",
                    30: "thirty",
                    40: "forty",
                    50: "fifty",
                    60: "sixty",
                    70: "seventy",
                    80: "eighty",
                    90: "ninety",
                },
                "scales": {100: "hundred", 1_000: "thousand", 1_000_000: "million"},
            },
        },
        "ta": {
            "max_number": 999_999,
            "supports_hyphens": False,
            "supports_and": False,
            "dictionary": {
                "units": {
                    0: "பூஜ்ஜியம்",
                    1: "ஒன்று",
                    2: "இரண்டு",
                    3: "மூன்று",
                    4: "நான்கு",
                    5: "ஐந்து",
                    6: "ஆறு",
                    7: "ஏழு",
                    8: "எட்டு",
                    9: "ஒன்பது",
                },
                "tens": {
                    10: "பத்து",
                    20: "இருபது",
                    30: "முப்பது",
                    40: "நாற்பது",
                    50: "ஐம்பது",
                    60: "அறுபது",
                    70: "எழுபது",
                    80: "எண்பது",
                    90: "தொண்ணூறு",
                },
                "scales": {100: "நூறு", 1_000: "ஆயிரம்", 100_000: "லட்சம்"},
            },
        },
    },
    # Domains to include in stress testing
    "stress_domains": [
        "arithmetic",
        "functions",
        "algebra",
        "geometry",
        "word_numbers",
        "story_single",
        "story_multi",
        "units_rates",
        "proportional",
        "mixed",
    ],
    # Load levels for stress testing
    "stress_levels": {
        "light": {
            "roundtrip": 1000,
            "noise": 500,
            "domains": 500,
            "templates": 100,
            "perf": 200,
        },
        "medium": {
            "roundtrip": 10_000,
            "noise": 5_000,
            "domains": 5_000,
            "templates": 1_000,
            "perf": 1_000,
        },
        "heavy": {
            "roundtrip": 50_000,
            "noise": 20_000,
            "domains": 20_000,
            "templates": 5_000,
            "perf": 5_000,
        },
        "extreme": {
            "roundtrip": 200_000,
            "noise": 100_000,
            "domains": 100_000,
            "templates": 20_000,
            "perf": 20_000,
        },
    },
}
