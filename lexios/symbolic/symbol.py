"""Implementation of Symbol class."""

from __future__ import annotations

from typing import Dict, Optional, TypeVar, Union

import sympy
import sympy as smp

from lexios.core.state import State


class _BaseSymbol(sympy.core.symbol.Symbol, State):
    """A symbolic representation of a symbol."""

    def __new__(cls, name: str):
        """New."""
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def __init__(self, *args):
        """Initialize the symbol."""
        State.__init__(self)

    def get_val_of_prop(self):
        """Return the value of the the problem that this symbol represents."""
        pass

    def eval(self):
        matter = self.get_state("matter")
        name = self.get_state("name")
        t = self.get_state("t")

        return matter.get_prop(name, t=t, eval=True)


class Symbol(_BaseSymbol):
    """A symbolic expression."""

    pass
