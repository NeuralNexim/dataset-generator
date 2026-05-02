import pytest
from math_dataset_generator.domains.arithmetic import generate_arithmetic_sample
from math_dataset_generator.domains.algebra import generate_algebra_sample
from math_dataset_generator.domains.geometry import generate_geometry_sample
from math_dataset_generator.domains.word_numbers import generate_word_numbers_sample
from math_dataset_generator.domains.story_single_step import (
    generate_story_single_step_sample,
)
from math_dataset_generator.domains.story_multi_step import (
    generate_story_multi_step_sample,
)
from math_dataset_generator.domains.units_rates import generate_units_rates_sample
from math_dataset_generator.domains.proportional import generate_proportional_sample
from math_dataset_generator.generator import generate_one_sample

DOMAINS = [
    generate_arithmetic_sample,
    generate_algebra_sample,
    generate_geometry_sample,
    generate_word_numbers_sample,
    generate_story_single_step_sample,
    generate_story_multi_step_sample,
    generate_units_rates_sample,
    generate_proportional_sample,
]


@pytest.mark.parametrize("fn", DOMAINS)
def test_domain_output_structure(fn):
    sample = fn()
    assert "domain" in sample
    assert "input" in sample
    assert "expression" in sample
    assert "reasoning" in sample
    assert "answer" in sample


def test_mixed_domain_output_structure():
    sample = generate_one_sample("mixed")
    assert "domain" in sample
    assert "input" in sample
    assert "expression" in sample
    assert "reasoning" in sample
    assert "answer" in sample
