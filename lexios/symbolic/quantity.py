"""Implementation of Quantity class."""

from __future__ import annotations


class Quantity:
    """Quantity class."""

    def __init__(self, value) -> None:
        """Initialize quantity."""
        self.value = value

    def __call__(self, *args, **kwargs):
        """Call."""
        return self.value

    def __repr__(self) -> str:
        """Representation."""
        return str(self.value)
