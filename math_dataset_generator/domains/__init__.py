from .arithmetic import generate_arithmetic_sample
from .functions import generate_functions_sample
from .word_numbers import generate_word_numbers_sample
from .story_single_step import generate_story_single_step_sample
from .story_multi_step import generate_story_multi_step_sample
from .units_rates import generate_units_rates_sample
from .proportional import generate_proportional_sample
from .geometry import generate_geometry_sample
from .algebra import generate_algebra_sample
from .mixed_domain import generate_mixed_sample
from .probability import generate_probability_sample
from .combinatorics import generate_combinatorics_sample
from .sequences import generate_sequences_sample
from .number_theory import generate_number_theory_sample
from .logic_puzzles import generate_logic_puzzles_sample
from .multi_step_algebra import generate_multi_step_algebra_sample
from .calculus import generate_calculus_sample
from .matrices import generate_matrices_sample
from .diagram_word_problems import generate_diagram_word_problems_sample

DOMAIN_REGISTRY = {
    "arithmetic": generate_arithmetic_sample,
    "functions": generate_functions_sample,
    "word_numbers": generate_word_numbers_sample,
    "story_single": generate_story_single_step_sample,
    "story_multi": generate_story_multi_step_sample,
    "units_rates": generate_units_rates_sample,
    "proportional": generate_proportional_sample,
    "geometry": generate_geometry_sample,
    "algebra": generate_algebra_sample,
    "mixed": generate_mixed_sample,
    # Section 2: New Domains
    "probability": generate_probability_sample,
    "combinatorics": generate_combinatorics_sample,
    "sequences": generate_sequences_sample,
    "number_theory": generate_number_theory_sample,
    "logic_puzzles": generate_logic_puzzles_sample,
    "multi_step_algebra": generate_multi_step_algebra_sample,
    "calculus": generate_calculus_sample,
    "matrices": generate_matrices_sample,
    "diagram_word_problems": generate_diagram_word_problems_sample,
}
