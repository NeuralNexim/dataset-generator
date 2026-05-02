.PHONY: test lint format typecheck run clean

test:
	pytest

lint:
	ruff math_dataset_generator tests

format:
	black math_dataset_generator tests

typecheck:
	mypy math_dataset_generator

run:
	python -m math_dataset_generator.main --domain arithmetic --n 10

clean:
	rm -rf .pytest_cache
	rm -rf build dist *.egg-info
