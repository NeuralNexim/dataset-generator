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
