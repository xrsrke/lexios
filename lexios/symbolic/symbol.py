from typing import (
    Dict,
    Union
)

import sympy
import sympy as smp


class _BaseSymbol(sympy.core.symbol.Symbol):
    """A symbolic representation of a symbol"""
    def __init__(self, *args):
        self._states: Dict[str, Union[str, float]] = dict()
    
    def __new__(cls, name: str):
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def add_state(self, name: str, value: Union[str, float]) -> None:
        self._states[name] = value
        
    def get_state(self, name: str) -> Union[str, float]:
        return self._states.get(name)

    @property
    def states(self) -> Dict[str, Union[str, float]]:
        return self._states

class Symbol(_BaseSymbol): pass