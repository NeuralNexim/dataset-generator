"""
Calculus Domain
Symbolic limits, power-rule derivatives, and definite integrals (text-only).
Keeps answers as exact integers or simple floats.
"""

import random

from math_dataset_generator.validation import assert_valid_answer
from math_dataset_generator.utils.curriculum_templates import get_template


def generate_calculus_sample(difficulty: str = "medium") -> dict:
    pattern = random.choice(["derivative", "integral", "limit"])

    if difficulty == "easy":
        a_range = (1, 4)
        n_range = (2, 3)
        int_a_range = (1, 5)
        int_b_range = (1, 5)
        lim_a_range = (1, 3)
        lim_b_range = (0, 5)
        lim_c_range = (1, 5)
    elif difficulty == "hard":
        a_range = (5, 15)
        n_range = (4, 8)
        int_a_range = (5, 20)
        int_b_range = (5, 20)
        lim_a_range = (5, 15)
        lim_b_range = (0, 20)
        lim_c_range = (5, 15)
    elif difficulty == "olympiad":
        a_range = (8, 20)
        n_range = (6, 12)
        int_a_range = (10, 50)
        int_b_range = (10, 50)
        lim_a_range = (10, 30)
        lim_b_range = (0, 50)
        lim_c_range = (10, 30)
    else:  # medium
        a_range = (1, 8)
        n_range = (2, 5)
        int_a_range = (1, 10)
        int_b_range = (1, 10)
        lim_a_range = (1, 6)
        lim_b_range = (0, 10)
        lim_c_range = (1, 8)

    if pattern == "derivative":
        # d/dx (a * x^n) = a*n * x^(n-1); evaluate at x=1 for integer answer
        a = random.randint(*a_range)
        n = random.randint(*n_range)
        coeff = a * n
        new_exp = n - 1
        answer = coeff * (1**new_exp)  # always coeff when x=1
        question = get_template("calculus", "derivative", difficulty).format(a=a, n=n)
        expression = f"d/dx({a}*x^{n}) at x=1"
        reasoning = (
            f"Using the power rule: f'(x) = {a}*{n}*x^{n-1} = {coeff}x^{new_exp}. "
            f"At x=1: f'(1) = {answer}."
        )

    elif pattern == "integral":
        # ∫_0^b (a) dx = a*b  (constant integrand, integer answer)
        a = random.randint(*int_a_range)
        b = random.randint(*int_b_range)
        answer = a * b
        question = get_template("calculus", "integral", difficulty).format(a=a, b=b)
        expression = f"integral({a}, 0, {b})"
        reasoning = f"∫₀^{b} {a} dx = [{a}x]₀^{b} = {a}×{b} - {a}×0 = {answer}."

    else:  # limit
        # lim_{x→c} (ax + b) = a*c + b
        a = random.randint(*lim_a_range)
        b = random.randint(*lim_b_range)
        c = random.randint(*lim_c_range)
        answer = a * c + b
        question = get_template("calculus", "limit", difficulty).format(a=a, b=b, c=c)
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
        "difficulty": difficulty,
    }
