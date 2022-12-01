"""Implementation of Symbol class."""

from __future__ import annotations

from typing import Dict, Optional, TypeVar, Union

import sympy
import sympy as smp

from lexios.core.state import State

T = TypeVar("T")


class _BaseSymbol(sympy.core.symbol.Symbol, State):
    """A symbolic representation of a symbol."""

    def __new__(cls, name: str):
        """New."""
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def __init__(self, *args):
        """Initialize the symbol."""
        State.__init__(self)

        self._states: Dict[str, T] = dict()

    def get_val_of_prop(self):
        """Return the value of the the problem that this symbol represents."""
        pass

    def eval(self):
        matter = self.get_state("matter")
        name = self.get_state("name")
        t = self.get_state("t")

        return matter.get_prop(name, t=t, eval=True)

    # def set_state(self, name: str, value: T):
    #     """Add state.

    #     Args:
    #         name (str): name of state
    #         value (T): value of state
    #     """
    #     self._states[name] = value

    # def get_state(self, name: str) -> Optional[Dict[str, T]]:
    #     """Get state.

    #     Args:
    #         name (str): name of state

    #     Returns:
    #         Dict[str, T]: value of state
    #     """
    #     return self._states.get(name)

    # @property
    # def states(self) -> Dict[str, str | T]:
    #     """Return all states.

    #     Returns:
    #         Dict[str, Union[str, T]]: _description_
    #     """
    #     return self._states


class Symbol(_BaseSymbol):
    """A symbolic expression."""

    pass
