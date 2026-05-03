"""
Calculus Domain
Symbolic limits, power-rule derivatives, and definite integrals (text-only).
Keeps answers as exact integers or simple floats.
"""

import random

from math_dataset_generator.validation import assert_valid_answer


def generate_calculus_sample() -> dict:
    pattern = random.choice(["derivative", "integral", "limit"])

    if pattern == "derivative":
        # d/dx (a * x^n) = a*n * x^(n-1); evaluate at x=1 for integer answer
        a = random.randint(1, 8)
        n = random.randint(2, 5)
        coeff = a * n
        new_exp = n - 1
        answer = coeff * (1 ** new_exp)   # always coeff when x=1
        question = (
            f"Find the derivative of f(x) = {a}x^{n} with respect to x, "
            f"then evaluate at x = 1."
        )
        expression = f"d/dx({a}*x^{n}) at x=1"
        reasoning = (
            f"Using the power rule: f'(x) = {a}*{n}*x^{n-1} = {coeff}x^{new_exp}. "
            f"At x=1: f'(1) = {answer}."
        )

    elif pattern == "integral":
        # ∫_0^b (a) dx = a*b  (constant integrand, integer answer)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = a * b
        question = (
            f"Evaluate the definite integral of f(x) = {a} from x = 0 to x = {b}."
        )
        expression = f"integral({a}, 0, {b})"
        reasoning = (
            f"∫₀^{b} {a} dx = [{a}x]₀^{b} = {a}×{b} - {a}×0 = {answer}."
        )

    else:  # limit
        # lim_{x→c} (ax + b) = a*c + b
        a = random.randint(1, 6)
        b = random.randint(0, 10)
        c = random.randint(1, 8)
        answer = a * c + b
        question = (
            f"Find the limit of f(x) = {a}x + {b} as x approaches {c}."
        )
        expression = f"lim(x→{c}) {a}x + {b}"
        reasoning = (
            f"Since f(x) = {a}x + {b} is continuous, lim_{{x→{c}}} f(x) = "
            f"{a}×{c} + {b} = {answer}."
        )

    assert_valid_answer(answer, "calculus")
    return {
        "domain": "calculus",
        "input": question,
        "expression": expression,
        "reasoning": reasoning,
        "answer": answer,
    }
