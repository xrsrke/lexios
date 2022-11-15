from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Union

import lexios.core.law as law
from lexios import matter
from lexios.symbolic.symbol import Symbol
from lexios.unit import Unit
from lexios.utils import camel_to_snake


class PropertyData(dict): pass
class _BaseProperty:
    def __init__(self):
        self.abrv: str | None = None
        self.unit: Unit | None = None
        self._data: PropertyData = PropertyData()
        self._laws: dict[str, law.Law] = dict()
        self._matter: matter.Matter | None = None

    @classmethod
    def class_name(cls) -> str:
        return camel_to_snake(cls.__name__)

    def symbol(self) -> Symbol:
        """Return a symbolic expression of this property"""
        symbol = Symbol(f'{self.abrv}')
        return symbol

    def get_val(self, t: int) -> int | Symbol:
        """Get a value at a given time

        Args:
            t (int): time
        """
        return self._data[t]['val'] if t in self._data else self.symbol()

    def set_val(self, val: str | int, t: int):
        """Set the value at a given time for property

        Args:
            val (Union[str, int]): value
            t (int): time
        """
        self._data[t] = {'val': val}

    @property
    def laws(self) -> dict[str, law.Law]:
        return self._laws

    def add_law(self, law: law.Law):
        assert isinstance(law, law), f"Expected law to be a Law, got {type(law)}"

        name = law.class_name()
        if self._laws and not name in self._laws:
            self._laws[name] = law

    def remove_law(self, name: str):
        """
        Docstring.remove_law(self, name: str
        """
        pass

    @property
    def matter(self) -> matter.Matter | None:
        """An property can't exists without matter."""
        return self._matter

    @matter.setter
    def matter(self, matter: matter.Matter):
        assert isinstance(matter, matter), f"Expected matter to be a Matter, but got {type(matter)}"
        self._matter = matter

    def __repr__(self) -> str:
        return f"{self.class_name().capitalize()}"

class Property(_BaseProperty):
    """Base class for all properties in matter"""
    pass

class PropList:
    """Holds all properties in a list"""
    def __init__(self, props: list[Property] = None):
        self._props: dict[str, Property] = {}

        if props is not None:
            for prop in props:
                name = prop.class_name()
                self._props[name] = prop

    @property
    def props(self) -> dict[str, Property]:
        return self._props

    def __len__(self) -> int:
        return len(self.props)

    def __iter__(self) -> Iterable[str, Property]:
        return iter(self.props.items())

class Mass(Property):
    """Mass Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'm'
        self.unit = Unit.MASS

class Mole(Property):
    """Mole Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'n'
        self.unit = Unit.MOLE

class Force(Property):
    """Force Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'F'
        self.unit = Unit.FORCE

class Acceleration(Property):
    """Acceleration Property"""
    def __init__(self):
        super().__init__()
        self.abrv = 'a'
        self.unit = Unit.ACCELERATION

def create_property_belongs_to_matter(prop, law, matter):
    assert isinstance(prop, Property) == True
    assert isinstance(law, law.Law) == True
    assert issubclass(matter, matter.Matter) == True

    p = prop()
    p.add_law(law)
    p.matter(matter)
