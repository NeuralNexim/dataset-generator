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
}
