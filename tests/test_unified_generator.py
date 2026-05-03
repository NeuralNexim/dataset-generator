import pytest

from math_dataset_generator.generator import generate_dataset


def test_unified_generator_basic():
    data = generate_dataset("arithmetic", 5)
    assert len(data) == 5
    for row in data:
        assert "domain" in row
        assert "input" in row
        assert "answer" in row
        assert "reasoning" in row
        assert "expression" in row


def test_domain_curriculum_schedule_progression():
    data = generate_dataset(
        "algebra", 8, seed=1, curriculum_schedule="domain_progressive"
    )
    assert len(data) == 8
    assert data[0]["difficulty"] == "easy"
    assert data[-1]["difficulty"] == "olympiad"
    assert all("curriculum_stage" in row for row in data)


def test_mixed_curriculum_schedule_adds_source_domain():
    data = generate_dataset(
        "mixed", 12, seed=3, curriculum_schedule="mixed_progressive"
    )
    assert len(data) == 12
    assert all(row["domain"] == "mixed" for row in data)
    assert all("source_domain" in row for row in data)
    assert all(row["source_domain"] != "mixed" for row in data)
    assert all("curriculum_stage" in row for row in data)


def test_unknown_curriculum_schedule_raises():
    with pytest.raises(ValueError):
        generate_dataset("arithmetic", 3, curriculum_schedule="missing_schedule")
