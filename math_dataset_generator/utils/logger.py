"""
Centralised logging configuration for math_dataset_generator.

Usage inside any module:
    from math_dataset_generator.utils.logger import get_logger
    log = get_logger(__name__)
    log.debug("generating sample for domain %s", domain)
"""

import logging


_PACKAGE = "math_dataset_generator"
_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
_DATE_FORMAT = "%H:%M:%S"


def get_logger(name: str) -> logging.Logger:
    """Return a child logger under the package root."""
    return logging.getLogger(name)


def configure_logging(debug: bool = False) -> None:
    """Configure the package-level logger.

    Call once at CLI entry-point startup.

    Args:
        debug: When True, set level to DEBUG and emit to stderr.
               When False, only WARNING and above are shown.
    """
    root = logging.getLogger(_PACKAGE)
    if root.handlers:
        return  # already configured

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(_FORMAT, datefmt=_DATE_FORMAT))
    root.addHandler(handler)
    root.setLevel(logging.DEBUG if debug else logging.WARNING)
