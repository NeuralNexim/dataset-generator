"""
Number Theory Domain
GCD, LCM, prime checking, divisibility.
"""

import random
import math

from math_dataset_generator.validation import assert_valid_answer


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


def generate_number_theory_sample() -> dict:
    pattern = random.choice(["gcd", "lcm", "prime_check", "divisibility"])

    if pattern == "gcd":
        a = random.randint(6, 60)
        b = random.randint(6, 60)
        answer = math.gcd(a, b)
        question = f"What is the greatest common divisor (GCD) of {a} and {b}?"
        expression = f"GCD({a}, {b})"
        reasoning = f"Using the Euclidean algorithm: GCD({a}, {b}) = {answer}."

    elif pattern == "lcm":
        a = random.randint(3, 20)
        b = random.randint(3, 20)
        answer = math.lcm(a, b)
        question = f"What is the least common multiple (LCM) of {a} and {b}?"
        expression = f"LCM({a}, {b})"
        reasoning = f"LCM({a}, {b}) = {a} × {b} / GCD({a},{b}) = {answer}."

    elif pattern == "prime_check":
        # pick a number and give a binary 1/0 answer
        n = random.randint(2, 50)
        is_p = _is_prime(n)
        answer = 1 if is_p else 0
        verdict = "prime" if is_p else "not prime"
        question = f"Is {n} a prime number? Answer 1 for yes, 0 for no."
        expression = f"is_prime({n})"
        reasoning = f"{n} is {verdict}."

    else:  # divisibility
        divisor = random.randint(2, 9)
        quotient = random.randint(2, 15)
        n = divisor * quotient
        answer = quotient
        question = f"How many times does {divisor} divide evenly into {n}?"
        expression = f"{n} // {divisor}"
        reasoning = f"{n} ÷ {divisor} = {answer} with remainder 0."

    assert_valid_answer(answer, "number_theory")
    return {
        "domain": "number_theory",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
