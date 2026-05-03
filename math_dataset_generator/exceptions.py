"""
Unified exception hierarchy for math_dataset_generator.

All public exceptions inherit from MathDatasetError so callers can
catch the whole family with a single except clause if needed.
"""


class MathDatasetError(Exception):
    """Base class for all library exceptions."""


class DomainError(MathDatasetError):
    """Raised when a domain generator produces an invalid or impossible result."""


class TemplateError(MathDatasetError):
    """Raised when a template cannot be rendered (missing keys, bad format)."""


class ReasoningError(MathDatasetError):
    """Raised when a reasoning-step builder receives invalid or incomplete input."""


class SampleValidationError(MathDatasetError):
    """Raised when a generated sample fails schema or invariant validation."""
