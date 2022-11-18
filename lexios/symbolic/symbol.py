"""Implementation of Symbol class."""

from __future__ import annotations

from typing import Dict, TypeVar, Union

import sympy
import sympy as smp

T = TypeVar("T")


class _BaseSymbol(sympy.core.symbol.Symbol):
    """A symbolic representation of a symbol."""

    def __new__(cls, name: str):
        """New."""
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def __init__(self, *args):
        """Initialize the symbol."""
        self._states: dict[str, T] = dict()

    def eval(self):
        matter = self.get_state("matter")
        name = self.get_state("name")
        t = self.get_state("t")

        return matter.get_prop(name, t=t, eval=True)

    def set_state(self, name: str, value: T):
        """Add state.

        Args:
            name (str): name of state
            value (T): value of state
        """
        self._states[name] = value

    def get_state(self, name: str) -> dict[str, T]:
        """Get state.

        Args:
            name (str): name of state

        Returns:
            Dict[str, T]: value of state
        """
        return self._states.get(name)

    @property
    def states(self) -> dict[str, str | T]:
        """Return all states.

        Returns:
            Dict[str, Union[str, T]]: _description_
        """
        return self._states


class Symbol(_BaseSymbol):
    """A symbolic expression."""

    pass
