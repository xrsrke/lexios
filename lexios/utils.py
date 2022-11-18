"""A list of utility functions."""

from __future__ import annotations

import re

_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
_REV_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")


def camel_to_snake(
    text: str,  # the string that you want to convert
) -> str:  # converted string
    """Convert a string to snake style."""
    snake_text = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
    return snake_text.lower()


def str2fml(x: str) -> str:
    """Turn a string to a chemical formula.

    Args:
        x (str): string

    Returns:
        str: string
    """
    return x.translate(_SUB)


def fml2str(x: str) -> str:
    """Convert Unicode chemical formula to string."""
    return x.translate(_REV_SUB)
