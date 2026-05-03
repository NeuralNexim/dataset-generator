"""
Difficulty-progressive question templates for all domains.

Structure: TEMPLATES[domain][pattern][difficulty] = list[str]
For single-pattern domains the pattern key is "_default".

Template strings use Python str.format() named placeholders.
Callers render with: get_template(domain, pattern, difficulty).format(**vars)
"""

import random

# ---------------------------------------------------------------------------
# Template definitions
# ---------------------------------------------------------------------------

TEMPLATES: dict[str, dict[str, dict[str, list[str]]]] = {
    # -----------------------------------------------------------------------
    "arithmetic": {
        "add": {
            "easy": ["What is {a} + {b}?", "Add {a} and {b}. What is the result?"],
            "medium": ["Calculate {a} + {b}.", "Find the sum of {a} and {b}."],
            "hard": ["Evaluate: {a} + {b}.", "Compute the sum of {a} and {b}."],
            "olympiad": [
                "Find the exact value of {a} + {b}.",
                "Determine the sum: {a} + {b}.",
            ],
        },
        "sub": {
            "easy": ["What is {a} - {b}?", "Subtract {b} from {a}. What do you get?"],
            "medium": [
                "Calculate {a} \u2212 {b}.",
                "Find the difference of {a} and {b}.",
            ],
            "hard": ["Evaluate: {a} \u2212 {b}.", "Compute {a} minus {b}."],
            "olympiad": [
                "Find the exact value of {a} \u2212 {b}.",
                "Determine the difference: {a} \u2212 {b}.",
            ],
        },
        "mul": {
            "easy": [
                "What is {a} \u00d7 {b}?",
                "Multiply {a} by {b}. What is the answer?",
            ],
            "medium": ["Calculate {a} \u00d7 {b}.", "Find the product of {a} and {b}."],
            "hard": [
                "Evaluate: {a} \u00d7 {b}.",
                "Compute the product of {a} and {b}.",
            ],
            "olympiad": [
                "Find the exact value of {a} \u00d7 {b}.",
                "Determine the product: {a} \u00d7 {b}.",
            ],
        },
        "div": {
            "easy": [
                "What is {result} \u00f7 {b}?",
                "Divide {result} by {b}. What is the result?",
            ],
            "medium": [
                "Calculate {result} \u00f7 {b}.",
                "Find the quotient when {result} is divided by {b}.",
            ],
            "hard": [
                "Evaluate: {result} \u00f7 {b}.",
                "Compute {result} divided by {b}.",
            ],
            "olympiad": [
                "Find the exact quotient of {result} \u00f7 {b}.",
                "Determine: {result} \u00f7 {b}.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "algebra": {
        "_default": {
            "easy": ["Solve for x: {eq}", "Find x: {eq}"],
            "medium": ["Solve the equation: {eq}", "What value of x satisfies {eq}?"],
            "hard": ["Determine x satisfying: {eq}", "Find the solution to {eq}."],
            "olympiad": [
                "Given {eq}, find the exact value of x.",
                "Solve for the unknown x in: {eq}",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "geometry": {
        "rectangle_area": {
            "easy": ["What is the area of a rectangle with width {w} and height {h}?"],
            "medium": [
                "Find the area of a rectangle with width {w} and height {h}.",
                "Calculate the area of a {w}\u00d7{h} rectangle.",
            ],
            "hard": [
                "Calculate the area of a rectangle with dimensions {w} \u00d7 {h}.",
                "Determine the area of a rectangle: width = {w}, height = {h}.",
            ],
            "olympiad": [
                "Determine the area of a rectangle with width {w} units and height {h} units.",
                "Find A = w\u00d7h for width {w} and height {h}.",
            ],
        },
        "rectangle_perimeter": {
            "easy": [
                "What is the perimeter of a rectangle with width {w} and height {h}?"
            ],
            "medium": [
                "Find the perimeter of a rectangle with width {w} and height {h}.",
                "Calculate the perimeter of a {w}\u00d7{h} rectangle.",
            ],
            "hard": [
                "Calculate the perimeter of a rectangle with dimensions {w} and {h}.",
                "Determine P = 2(w+h) for width {w} and height {h}.",
            ],
            "olympiad": [
                "Determine the perimeter of a rectangle with width {w} units and height {h} units.",
                "Find P = 2({w}+{h}).",
            ],
        },
        "triangle_area": {
            "easy": ["What is the area of a triangle with base {b} and height {h}?"],
            "medium": [
                "Find the area of a triangle with base {b} and height {h}.",
                "Calculate the area of a triangle: base {b}, height {h}.",
            ],
            "hard": [
                "Calculate the area of a triangle with base {b} and height {h}.",
                "Using A = 0.5\u00d7b\u00d7h, find the area for base {b} and height {h}.",
            ],
            "olympiad": [
                "Determine the area of a triangle with base {b} units and height {h} units.",
                "Find A = \u00bd\u00d7{b}\u00d7{h}.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "word_numbers": {
        "_default": {
            "easy": ["Write {words} as a number.", "What number is '{words}'?"],
            "medium": [
                "Convert this number in words to digits: {words}",
                "Express '{words}' as a numeral.",
            ],
            "hard": [
                "Translate the word form '{words}' into its numeric representation.",
                "Write '{words}' as an integer.",
            ],
            "olympiad": [
                "Given the word representation '{words}', state the corresponding integer.",
                "Convert to digits: {words}",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "story_single": {
        "add": {
            "easy": [
                "{name} had {a} {obj} and got {b} more. How many {obj} does {name} have?"
            ],
            "medium": [
                "{name} had {a} {obj}. {name} got {b} more. How many {obj} does {name} have now?",
                "A bag had {a} {obj}. {b} more were added. How many {obj} are there?",
            ],
            "hard": [
                "Starting with {a} {obj}, {name} acquires {b} more. What is the total?",
                "If {name} begins with {a} {obj} and receives {b} more, what is the final count?",
            ],
            "olympiad": [
                "Given that {name} initially possesses {a} {obj} and subsequently acquires {b} more, "
                "determine the total number of {obj}.",
                "{name} starts with {a} {obj} and gains {b}. Find the total.",
            ],
        },
        "sub": {
            "easy": ["{name} had {a} {obj} and gave away {b}. How many are left?"],
            "medium": [
                "{name} had {a} {obj}. {name} gave away {b}. How many {obj} does {name} have now?",
                "A pile of {a} {obj} has {b} removed. How many remain?",
            ],
            "hard": [
                "Starting with {a} {obj}, {name} removes {b}. What remains?",
                "After giving {b} {obj} away from {a}, how many {obj} remain?",
            ],
            "olympiad": [
                "Given {a} {obj} and a reduction of {b}, determine the remaining count.",
                "{name} has {a} {obj} and distributes {b}. Find the remainder.",
            ],
        },
        "mul": {
            "easy": [
                "{name} has {a} bags with {b} {obj} each. How many {obj} in total?"
            ],
            "medium": [
                "{name} has {a} bags with {b} {obj} in each. How many {obj} does {name} have in total?",
                "There are {a} groups of {b} {obj}. How many {obj} altogether?",
            ],
            "hard": [
                "Calculate the total number of {obj} if there are {a} groups of {b}.",
                "{a} sets each contain {b} {obj}. What is the total count?",
            ],
            "olympiad": [
                "Given {a} collections each containing {b} {obj}, determine the aggregate total.",
                "Find the product: {a} groups \u00d7 {b} {obj} per group.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "story_multi": {
        "add_add": {
            "easy": [
                "{name} had {a} {obj}, got {b} more, then found {c} more. How many total?"
            ],
            "medium": [
                "{name} had {a} {obj}. {name} got {b} more. Then {name} found {c} more. "
                "How many {obj} does {name} have now?"
            ],
            "hard": [
                "Starting with {a} {obj}, then gaining {b} and then {c}, what is the final total?"
            ],
            "olympiad": [
                "Given an initial count of {a} {obj}, two successive additions of {b} and {c}, "
                "determine the final total."
            ],
        },
        "add_sub": {
            "easy": [
                "{name} had {a} {obj}, got {b} more, then gave away {c}. How many remain?"
            ],
            "medium": [
                "{name} had {a} {obj}. {name} got {b} more. Then {name} gave away {c}. "
                "How many {obj} does {name} have now?"
            ],
            "hard": [
                "After gaining {b} {obj} from {a}, then removing {c}, what is the final count?"
            ],
            "olympiad": [
                "Given {a} {obj} augmented by {b} then reduced by {c}, determine the final value."
            ],
        },
        "sub_add": {
            "easy": [
                "{name} had {a} {obj}, gave away {b}, then got {c} more. How many now?"
            ],
            "medium": [
                "{name} had {a} {obj}. {name} gave away {b}. Then {name} got {c} more. "
                "How many {obj} does {name} have now?"
            ],
            "hard": [
                "From {a} {obj}, subtract {b} then add {c}. What is the final count?"
            ],
            "olympiad": [
                "Starting with {a} {obj}, after a loss of {b} and a subsequent gain of {c}, "
                "determine the final total."
            ],
        },
    },
    # -----------------------------------------------------------------------
    "units_rates": {
        "speed": {
            "easy": ["A car goes {speed} km/h for {time} hours. How far does it go?"],
            "medium": [
                "A car travels at {speed} km/h for {time} hours. How far does it travel?",
                "At a speed of {speed} km/h, how far is covered in {time} hours?",
            ],
            "hard": [
                "Calculate the distance covered by a vehicle moving at {speed} km/h for {time} hours.",
                "Determine the total distance if speed is {speed} km/h and time is {time} h.",
            ],
            "olympiad": [
                "A body moving at constant velocity {speed} km/h for {time} hours: find the displacement.",
                "Given speed = {speed} km/h and time = {time} h, compute the distance.",
            ],
        },
        "rate": {
            "easy": [
                "A machine makes {rate} items per hour. How many in {hours} hours?"
            ],
            "medium": [
                "A machine produces {rate} items per hour. How many items in {hours} hours?",
                "At a rate of {rate} items/hour, how many items are produced in {hours} hours?",
            ],
            "hard": [
                "Calculate total production if a machine runs at {rate} items/hour for {hours} hours.",
                "Determine output: {rate} items per hour over {hours} hours.",
            ],
            "olympiad": [
                "Given a constant production rate of {rate} units per hour over {hours} hours, "
                "find the total output.",
                "Compute: rate {rate} items/h \u00d7 duration {hours} h.",
            ],
        },
        "conversion": {
            "easy": ["How many kilometers is {meters} meters?"],
            "medium": [
                "Convert {meters} meters to kilometers.",
                "Express {meters} m in km.",
            ],
            "hard": [
                "Convert {meters} metres to kilometres.",
                "Calculate the equivalent of {meters} m in km.",
            ],
            "olympiad": [
                "Express {meters} metres in kilometres, giving the exact decimal value.",
                "Convert: {meters} m \u2192 km.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "proportional": {
        "_default": {
            "easy": ["If {a} apples cost {b} dollars, what do {a2} apples cost?"],
            "medium": [
                "If {a} apples cost {b} dollars, how much do {a2} apples cost?",
                "Given {a} items cost {b}, find the cost of {a2} items.",
            ],
            "hard": [
                "Using proportional reasoning: if {a} units cost {b}, "
                "what is the cost of {a2} units?",
                "Calculate the cost of {a2} items if {a} items cost {b}.",
            ],
            "olympiad": [
                "Given a linear proportional relationship where {a} items cost {b} units of currency, "
                "determine the cost of {a2} items.",
                "Determine: if cost({a}) = {b}, find cost({a2}).",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "functions": {
        "_default": {
            "easy": ["If f(x) = {expr}, what is f({x})?"],
            "medium": [
                "If f(x) = {expr}, what is f({x})?",
                "Evaluate f({x}) for f(x) = {expr}.",
            ],
            "hard": [
                "Given f(x) = {expr}, compute f({x}).",
                "Evaluate the function f(x) = {expr} at x = {x}.",
            ],
            "olympiad": [
                "For the function f(x) = {expr}, determine the value of f({x}).",
                "Given f: x \u21a6 {expr}, find f({x}).",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "probability": {
        "coin": {
            "easy": ["A coin is flipped. What is the chance of getting {side}?"],
            "medium": [
                "A fair coin is flipped. What is the probability of getting {side}?",
                "Flip a fair coin once. What is P({side})?",
            ],
            "hard": [
                "Calculate the probability of {side} when a fair coin is tossed once.",
                "Determine P(outcome = {side}) for a single fair coin toss.",
            ],
            "olympiad": [
                "For a single toss of a fair coin, determine the probability of the outcome being {side}.",
                "Find P({side}) for one fair coin flip.",
            ],
        },
        "dice": {
            "easy": ["You roll a die. What is the chance of rolling {target}?"],
            "medium": [
                "A fair six-sided die is rolled. What is the probability of rolling a {target}?",
                "Roll a fair die. What is P(rolling {target})?",
            ],
            "hard": [
                "Calculate the probability of rolling exactly {target} on a fair six-sided die.",
                "Determine P(outcome = {target}) for one roll of a fair die.",
            ],
            "olympiad": [
                "For a single roll of a fair six-sided die, determine the probability of "
                "the outcome being {target}.",
                "Find P(X = {target}) where X is uniform on {{1,2,3,4,5,6}}.",
            ],
        },
        "balls": {
            "easy": [
                "A bag has {red} red and {blue} blue balls. "
                "What is the chance of drawing a {colour} one?"
            ],
            "medium": [
                "A bag contains {red} red balls and {blue} blue balls. "
                "One ball is drawn at random. What is the probability it is {colour}?",
                "From {total} balls ({red} red, {blue} blue), find P(drawing {colour}).",
            ],
            "hard": [
                "Calculate the probability of selecting a {colour} ball at random "
                "from a bag with {red} red and {blue} blue balls.",
                "Determine P({colour}) when drawing from {red} red + {blue} blue balls.",
            ],
            "olympiad": [
                "A bag contains {red} red and {blue} blue balls. "
                "One is drawn uniformly at random. Determine P(ball is {colour}).",
                "Find P({colour}) from a uniform draw over {total} balls "
                "({red} red, {blue} blue).",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "combinatorics": {
        "permutation": {
            "easy": [
                "How many ways can you arrange {r} items from {n} items (order matters)?"
            ],
            "medium": [
                "How many ways can {r} items be arranged from a set of {n} distinct items "
                "(order matters)?",
                "In how many ways can {r} objects be selected and arranged from {n} objects?",
            ],
            "hard": [
                "Compute P({n},{r}): the number of ordered arrangements of {r} items from {n}.",
                "Find the number of permutations of {r} items chosen from {n} distinct items.",
            ],
            "olympiad": [
                "Determine the number of permutations P({n},{r}) = {n}!/({n}-{r})!.",
                "How many ordered selections of {r} from {n} distinct items exist?",
            ],
        },
        "combination": {
            "easy": [
                "How many ways can you choose {r} items from {n} (order doesn't matter)?"
            ],
            "medium": [
                "How many ways can {r} items be chosen from a set of {n} distinct items "
                "(order does not matter)?",
                "Find C({n},{r}): choosing {r} from {n}.",
            ],
            "hard": [
                "Compute the binomial coefficient C({n},{r}).",
                "Determine the number of combinations of {r} items from {n} distinct items.",
            ],
            "olympiad": [
                "Evaluate C({n},{r}) = {n}!/({r}!\u00b7({n}-{r})!).",
                "Find the number of unordered subsets of size {r} from a set of {n} elements.",
            ],
        },
        "counting": {
            "easy": [
                "There are {c0} choices for item 1 and {c1} for item 2. How many combinations?"
            ],
            "medium": [
                "There are {c0} choices for the first item and {c1} choices for the second item. "
                "How many combinations are there in total?"
            ],
            "hard": [
                "Using the multiplication principle: {c0} options \u00d7 {c1} options. Find the total.",
                "Apply the fundamental counting principle: {c0} \u00d7 {c1}.",
            ],
            "olympiad": [
                "By the multiplication principle, determine the total number of outcomes "
                "given {c0} choices for the first event and {c1} for the second.",
                "Compute the Cartesian product size: |A| = {c0}, |B| = {c1}.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "sequences": {
        "arith_nth": {
            "easy": [
                "A sequence starts at {a} and increases by {d} each time. What is term {n}?"
            ],
            "medium": [
                "An arithmetic sequence has first term {a} and common difference {d}. "
                "What is the {n}th term?",
                "Find the {n}th term of an arithmetic sequence: first term {a}, difference {d}.",
            ],
            "hard": [
                "Determine the {n}th term of an arithmetic progression with a\u2081 = {a} and d = {d}.",
                "Calculate T_{n} for the arithmetic sequence where a = {a} and d = {d}.",
            ],
            "olympiad": [
                "For the arithmetic sequence with first term {a} and common difference {d}, "
                "find the {n}th term using T\u2099 = a + (n\u22121)d.",
                "Given a = {a}, d = {d}, determine T_{n}.",
            ],
        },
        "arith_sum": {
            "easy": [
                "A sequence starts at {a} with step {d}. What is the sum of the first {n} terms?"
            ],
            "medium": [
                "Find the sum of the first {n} terms of an arithmetic sequence "
                "with first term {a} and common difference {d}.",
                "Calculate S_{n} for arithmetic seq: a = {a}, d = {d}, n = {n}.",
            ],
            "hard": [
                "Determine S_{n} for an arithmetic progression with a\u2081 = {a}, d = {d}, n = {n}.",
                "Compute the sum of the first {n} terms: a = {a}, d = {d}.",
            ],
            "olympiad": [
                "Using S\u2099 = n/2\u00b7(2a+(n\u22121)d), find S_{n} for a = {a}, d = {d}, n = {n}.",
                "Find S_{n} for the AP with first term {a} and common difference {d}.",
            ],
        },
        "geo_nth": {
            "easy": [
                "A sequence starts at {a} and multiplies by {r} each time. What is term {n}?"
            ],
            "medium": [
                "A geometric sequence has first term {a} and common ratio {r}. "
                "What is the {n}th term?",
                "Find the {n}th term of a geometric sequence with a = {a} and r = {r}.",
            ],
            "hard": [
                "Determine the {n}th term of a geometric progression with a\u2081 = {a} and r = {r}.",
                "Calculate T_{n} = a\u00b7r^(n-1) for a = {a}, r = {r}, n = {n}.",
            ],
            "olympiad": [
                "For the geometric sequence with first term {a} and ratio {r}, "
                "find T\u2099 = a\u00b7r^(n\u22121) at n = {n}.",
                "Given a = {a}, r = {r}, compute T_{n}.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "number_theory": {
        "gcd": {
            "easy": ["What is the GCD of {a} and {b}?"],
            "medium": [
                "What is the greatest common divisor (GCD) of {a} and {b}?",
                "Find GCD({a}, {b}).",
            ],
            "hard": [
                "Compute GCD({a}, {b}) using the Euclidean algorithm.",
                "Determine the greatest common divisor of {a} and {b}.",
            ],
            "olympiad": [
                "Using the Euclidean algorithm, find GCD({a}, {b}).",
                "Determine gcd({a}, {b}).",
            ],
        },
        "lcm": {
            "easy": ["What is the LCM of {a} and {b}?"],
            "medium": [
                "What is the least common multiple (LCM) of {a} and {b}?",
                "Find LCM({a}, {b}).",
            ],
            "hard": [
                "Compute LCM({a}, {b}).",
                "Determine the least common multiple of {a} and {b}.",
            ],
            "olympiad": [
                "Using LCM(a,b) = a\u00b7b/GCD(a,b), find LCM({a}, {b}).",
                "Determine lcm({a}, {b}).",
            ],
        },
        "prime_check": {
            "easy": ["Is {n} a prime number? Answer 1 for yes, 0 for no."],
            "medium": [
                "Is {n} a prime number? Answer 1 for yes, 0 for no.",
                "Determine if {n} is prime. Give 1 if yes, 0 if no.",
            ],
            "hard": [
                "Is the integer {n} prime? Output 1 for prime, 0 for composite.",
                "Classify {n}: prime (1) or not prime (0)?",
            ],
            "olympiad": [
                "Determine whether {n} is prime. State 1 if it is, 0 otherwise.",
                "Is {n} \u2208 \u2119? Answer 1 (yes) or 0 (no).",
            ],
        },
        "divisibility": {
            "easy": ["How many times does {divisor} go into {n}?"],
            "medium": [
                "How many times does {divisor} divide evenly into {n}?",
                "Find {n} \u00f7 {divisor}.",
            ],
            "hard": [
                "Compute {n} \u00f7 {divisor} (exact integer division).",
                "Determine the quotient when {n} is divided by {divisor}.",
            ],
            "olympiad": [
                "Find the integer quotient of {n} \u00f7 {divisor}.",
                "Compute \u230a{n}/{divisor}\u230b.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "logic_puzzles": {
        "age_diff": {
            "easy": ["{n0} is {a0} and {n1} is {a1}. How many years older is {n0}?"],
            "medium": [
                "{n0} is {a0} years old and {n1} is {a1} years old. "
                "How many years older is {n0} than {n1}?",
                "Compare ages: {n0} is {a0}, {n1} is {a1}. What is the age difference?",
            ],
            "hard": [
                "Given {n0}'s age is {a0} and {n1}'s age is {a1}, "
                "compute the positive difference.",
                "Find |age({n0}) \u2212 age({n1})| given ages {a0} and {a1}.",
            ],
            "olympiad": [
                "Determine the absolute age difference between {n0} (age {a0}) "
                "and {n1} (age {a1}).",
                "Given ages {a0} and {a1}, find |{a0} \u2212 {a1}|.",
            ],
        },
        "age_sum": {
            "easy": ["{n0} is {a0} and {n1} is {a1}. What is the sum of their ages?"],
            "medium": [
                "{n0} is {a0} years old and {n1} is {a1} years old. "
                "What is the sum of their ages?",
                "Find the total age of {n0} ({a0}) and {n1} ({a1}).",
            ],
            "hard": [
                "Compute age({n0}) + age({n1}) given {a0} and {a1}.",
                "What is {a0} + {a1}?",
            ],
            "olympiad": [
                "Given {n0} aged {a0} and {n1} aged {a1}, find the sum of their ages.",
                "Determine {a0} + {a1}.",
            ],
        },
        "simple_deduction": {
            "easy": [
                "{name} has {start} coins, gives {give} away, gets {receive} back. "
                "How many now?"
            ],
            "medium": [
                "{name} has {start} coins. {name} gives away {give} and then receives "
                "{receive} more. How many coins does {name} have now?",
                "Starting with {start}, subtract {give} then add {receive}. "
                "What is the result?",
            ],
            "hard": [
                "Compute {start} \u2212 {give} + {receive}.",
                "Given initial value {start}, a deduction of {give}, and an addition of "
                "{receive}, find the final value.",
            ],
            "olympiad": [
                "Evaluate the expression: {start} \u2212 {give} + {receive}.",
                "Starting from {start}, apply \u2212{give} then +{receive}. "
                "Determine the result.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "multi_step_algebra": {
        "two_step": {
            "easy": ["Solve for x: {a}x + {b} = {c}"],
            "medium": ["Solve for x: {a}x + {b} = {c}", "Find x if {a}x + {b} = {c}."],
            "hard": [
                "Determine x satisfying: {a}x + {b} = {c}.",
                "Solve the linear equation {a}x + {b} = {c}.",
            ],
            "olympiad": [
                "Find the exact solution x for the equation {a}x + {b} = {c}.",
                "Given {a}x + {b} = {c}, determine x \u2208 \u211d.",
            ],
        },
        "substitution": {
            "easy": ["x + y = {s} and x - y = {d}. Find x."],
            "medium": [
                "Solve the system: x + y = {s} and x - y = {d}. What is x?",
                "Given x + y = {s} and x \u2212 y = {d}, find x.",
            ],
            "hard": [
                "Solve: x + y = {s}, x \u2212 y = {d}. Find x.",
                "Using substitution, determine x from x + y = {s} and x \u2212 y = {d}.",
            ],
            "olympiad": [
                "Given the linear system x + y = {s}, x \u2212 y = {d}, solve for x.",
                "Find x satisfying simultaneously: x + y = {s} and x \u2212 y = {d}.",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "calculus": {
        "derivative": {
            "easy": ["What is the derivative of {a}x^{n} at x = 1?"],
            "medium": [
                "Find the derivative of f(x) = {a}x^{n} with respect to x, "
                "then evaluate at x = 1.",
                "Differentiate f(x) = {a}x^{n} and evaluate f'(1).",
            ],
            "hard": [
                "Using the power rule, differentiate f(x) = {a}x^{n} and evaluate at x = 1.",
                "Compute d/dx({a}x^{n})|_{{x=1}}.",
            ],
            "olympiad": [
                "Determine f'(1) for f(x) = {a}x^{n} using the power rule.",
                "Evaluate d/dx[{a}x^{n}] at x = 1.",
            ],
        },
        "integral": {
            "easy": ["What is the area under f(x) = {a} from x = 0 to x = {b}?"],
            "medium": [
                "Evaluate the definite integral of f(x) = {a} from x = 0 to x = {b}.",
                "Find \u222b\u2080^{b} {a} dx.",
            ],
            "hard": [
                "Compute \u222b\u2080^{b} {a} dx.",
                "Evaluate the integral of the constant function f(x) = {a} over [0, {b}].",
            ],
            "olympiad": [
                "Determine \u222b\u2080^{b} {a} dx by applying the fundamental theorem of calculus.",
                "Compute the definite integral \u222b_0^{{{b}}} {a} dx.",
            ],
        },
        "limit": {
            "easy": ["What is f({c}) if f(x) = {a}x + {b}?"],
            "medium": [
                "Find the limit of f(x) = {a}x + {b} as x approaches {c}.",
                "Evaluate lim_{{x\u2192{c}}} ({a}x + {b}).",
            ],
            "hard": [
                "Compute lim_{{x\u2192{c}}} ({a}x + {b}).",
                "Determine the limit of {a}x + {b} as x \u2192 {c}.",
            ],
            "olympiad": [
                "Evaluate lim_{{x\u2192{c}}} f(x) for f(x) = {a}x + {b}.",
                "Find lim_{{x\u2192{c}}} ({a}x + {b}).",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "matrices": {
        "determinant": {
            "easy": ["Find the |det| of the 2\u00d72 matrix {mat}."],
            "medium": [
                "Find the determinant of the 2\u00d72 matrix {mat}. Give the absolute value.",
                "Compute |det({mat})|.",
            ],
            "hard": [
                "Calculate the absolute determinant of the matrix {mat}.",
                "Determine |det A| for A = {mat}.",
            ],
            "olympiad": [
                "For the matrix A = {mat}, compute |det(A)| = |ad \u2212 bc|.",
                "Evaluate |det({mat})|.",
            ],
        },
        "trace": {
            "easy": ["Add up the diagonal elements of the matrix {mat}."],
            "medium": [
                "Find the trace (sum of diagonal elements) of the matrix {mat}.",
                "Compute tr({mat}).",
            ],
            "hard": [
                "Calculate the trace of the matrix {mat}.",
                "Determine tr(A) for A = {mat}.",
            ],
            "olympiad": [
                "For the matrix A = {mat}, find tr(A) = a\u2081\u2081 + a\u2082\u2082.",
                "Evaluate the trace of {mat}.",
            ],
        },
        "scalar_mult": {
            "easy": ["Multiply the matrix {mat} by {k}. What is the top-left number?"],
            "medium": [
                "Multiply the matrix {mat} by scalar {k}. "
                "What is the value of the top-left element of the result?",
                "Compute the (1,1) entry of {k}\u00b7{mat}.",
            ],
            "hard": [
                "For scalar multiplication {k}\u00b7{mat}, determine the (0,0) element.",
                "Compute (k\u00b7A)[0,0] where k = {k} and A = {mat}.",
            ],
            "olympiad": [
                "Given A = {mat} and scalar k = {k}, find the top-left entry of kA.",
                "Determine ({k}\u00b7{mat})[0][0].",
            ],
        },
    },
    # -----------------------------------------------------------------------
    "diagram_word_problems": {
        "grid_distance": {
            "easy": [
                "On a grid, A is at ({x1},{y1}) and B is at ({x2},{y2}). "
                "Shortest path (horizontal/vertical only)?"
            ],
            "medium": [
                "On a grid, point A is at ({x1}, {y1}) and point B is at ({x2}, {y2}). "
                "Moving only horizontally or vertically, what is the shortest distance "
                "(in grid steps) from A to B?",
                "Find the Manhattan distance from ({x1},{y1}) to ({x2},{y2}).",
            ],
            "hard": [
                "Calculate the Manhattan (L\u00b9) distance between ({x1},{y1}) "
                "and ({x2},{y2}).",
                "Determine |\u0394x| + |\u0394y| from ({x1},{y1}) to ({x2},{y2}).",
            ],
            "olympiad": [
                "Compute the L\u00b9 (taxicab) distance between points "
                "({x1},{y1}) and ({x2},{y2}).",
                "Find |{x2}\u2212{x1}| + |{y2}\u2212{y1}|.",
            ],
        },
        "clock_hours": {
            "easy": ["A clock shows {h1}:00. How many hours until {h2}:00?"],
            "medium": [
                "A clock shows {h1}:00. How many hours later will it show {h2}:00?",
                "From {h1}:00 to {h2}:00, how many hours pass?",
            ],
            "hard": [
                "Calculate the elapsed hours from {h1}:00 to {h2}:00.",
                "Determine {h2} \u2212 {h1}.",
            ],
            "olympiad": [
                "Find the difference in hours between {h1}:00 and {h2}:00 "
                "on a 12-hour clock.",
                "Compute {h2} \u2212 {h1}.",
            ],
        },
        "coordinate_distance": {
            "easy": [
                "A is at ({x1},{y1}) and B is at ({x2},{y2}). How far apart are they?"
            ],
            "medium": [
                "Point A is at ({x1}, {y1}) and point B is at ({x2}, {y2}). "
                "What is the straight-line (Euclidean) distance between A and B?",
                "Find the distance from ({x1},{y1}) to ({x2},{y2}).",
            ],
            "hard": [
                "Compute the Euclidean distance between ({x1},{y1}) and ({x2},{y2}).",
                "Using the distance formula, find |AB| for "
                "A=({x1},{y1}), B=({x2},{y2}).",
            ],
            "olympiad": [
                "Determine the Euclidean distance d(A,B) = "
                "\u221a((x\u2082\u2212x\u2081)\u00b2+(y\u2082\u2212y\u2081)\u00b2) "
                "for A=({x1},{y1}) and B=({x2},{y2}).",
                "Compute |AB| for A=({x1},{y1}), B=({x2},{y2}).",
            ],
        },
    },
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def get_template(domain: str, pattern: str, difficulty: str) -> str:
    """
    Return a random question template string for (domain, pattern, difficulty).

    Falls back gracefully:
      - Unknown pattern  → tries '_default', else returns empty string.
      - Unknown difficulty → falls back to 'medium'.
    """
    domain_tpl = TEMPLATES.get(domain, {})
    pattern_tpl = domain_tpl.get(pattern, domain_tpl.get("_default", {}))
    options = pattern_tpl.get(difficulty, pattern_tpl.get("medium", [""]))
    return random.choice(options)
