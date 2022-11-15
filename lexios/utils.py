from __future__ import annotations

import re

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
REV_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")


def camel_to_snake(
    name: str,  # the string that you want to convert
) -> str:  # converted string
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def str2fml(x: str) -> str:
    """Turn a string to a chemical formula

    Args:
        x (str): string

    Returns:
        str: string
    """
    return x.translate(SUB)


def fml2str(x: str) -> str:
    return x.translate(REV_SUB)
