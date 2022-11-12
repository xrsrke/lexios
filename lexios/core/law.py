from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional

import lexios.matter as matter
from lexios.utils import camel_to_snake

if TYPE_CHECKING:
    from lexios.core.property import Property


class _BaseLaw(ABC):
    def __init__(self) -> None:
        self._props: Dict[str, Property] = dict()
        self._matter: Optional[matter.Matter] = None
    
    @property
    def props(self) -> Dict[str, Property]:
        return self._props
    
    def add_props_to_matter(self, value: matter.Matter):
        """Add all properties that belongs to this law to the matter

        Args:
            matter (_type_): Matter
        """
        
        assert isinstance(value, matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"
        
        if not self.props:
            for prop in self.props:
                value.add_prop(prop)
    
    def add_law_to_matter(self, value: matter.Matter):
        """Add this law to the matter

        Args:
            matter (_type_): Matter
        """
        assert isinstance(value, matter.Matter), f"Expected matter to be Matter, got {type(matter)}"
        value.add_law(self)
        self.add_props_to_matter(value)
    
    @property
    def matter(self):
        return self._matter
    
    @matter.setter
    def matter(self, value: matter.Matter):
        assert isinstance(value, matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"
        self._matter = value
    
    @classmethod
    def class_name(cls) -> str:  # return the snake style name
        return camel_to_snake(cls.__name__)
    
    @abstractclassmethod
    def expr(self): pass


class Law(_BaseLaw): pass


class ConstantGas(Law): pass