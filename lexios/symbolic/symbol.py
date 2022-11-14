from typing import (
    Dict,
    Union,
    TypeVar
)

import sympy
import sympy as smp

T = TypeVar("T")

class _BaseSymbol(sympy.core.symbol.Symbol):
    """A symbolic representation of a symbol"""
    def __init__(self, *args):
        self._states: Dict[str, T] = dict()
    
    def __new__(cls, name: str):
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def add_state(self, name: str, value: T):
        """Add state

        Args:
            name (str): name of state
            value (T): value of state
        """
        self._states[name] = value
        
    def get_state(self, name: str) -> Dict[str, T]:
        """Get state

        Args:
            name (str): name of state

        Returns:
            Dict[str, T]: value of state
        """
        return self._states.get(name)

    @property
    def states(self) -> Dict[str, Union[str, T]]:
        """Return all states

        Returns:
            Dict[str, Union[str, T]]: _description_
        """
        return self._states

class Symbol(_BaseSymbol): pass