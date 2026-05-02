"""
Stress testing package for math_dataset_generator.
Provides CLI entrypoint and programmatic access.
"""

from .cli import main as run_stress

__all__ = ["run_stress"]
