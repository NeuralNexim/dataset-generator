"""
Number Theory Domain
GCD, LCM, prime checking, divisibility.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_number_theory_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["gcd", "lcm", "prime_check", "divisibility"])

    if difficulty == "easy":
        lo, hi = 4, 30
        prime_range = (2, 30)
        div_range = (2, 6)
        div_q_range = (2, 8)
    elif difficulty == "hard":
        lo, hi = 20, 200
        prime_range = (2, 100)
        div_range = (2, 15)
        div_q_range = (5, 30)
    elif difficulty == "olympiad":
        lo, hi = 100, 1000
        prime_range = (2, 200)
        div_range = (7, 29)
        div_q_range = (10, 50)
    else:  # medium
        lo, hi = 6, 60
        prime_range = (2, 50)
        div_range = (2, 9)
        div_q_range = (2, 15)

    if pattern == "gcd":
        a = random.randint(lo, hi)
        b = random.randint(lo, hi)
        answer = math.gcd(a, b)
        question = get_template("number_theory", "gcd", difficulty).format(a=a, b=b)
        expression = f"GCD({a}, {b})"
        reasoning = f"Using the Euclidean algorithm: GCD({a}, {b}) = {answer}."

    elif pattern == "lcm":
        a = random.randint(lo // 3, hi // 3)
        b = random.randint(lo // 3, hi // 3)
        answer = math.lcm(a, b)
        question = get_template("number_theory", "lcm", difficulty).format(a=a, b=b)
        expression = f"LCM({a}, {b})"
        reasoning = f"LCM({a}, {b}) = {a} × {b} / GCD({a},{b}) = {answer}."

    elif pattern == "prime_check":
        # pick a number and give a binary 1/0 answer
        n = random.randint(*prime_range)
        is_p = _is_prime(n)
        answer = 1 if is_p else 0
        verdict = "prime" if is_p else "not prime"
        question = get_template("number_theory", "prime_check", difficulty).format(n=n)
        expression = f"is_prime({n})"
        reasoning = f"{n} is {verdict}."

    else:  # divisibility
        divisor = random.randint(*div_range)
        quotient = random.randint(*div_q_range)
        n = divisor * quotient
        answer = quotient
        question = get_template("number_theory", "divisibility", difficulty).format(
            divisor=divisor, n=n
        )
        expression = f"{n} // {divisor}"
        reasoning = f"{n} ÷ {divisor} = {answer} with remainder 0."

    assert_valid_answer(answer, "number_theory")
    return {
        "domain": "number_theory",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
        "difficulty": difficulty,
    }
