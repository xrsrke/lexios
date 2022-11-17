from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Union

import lexios.core.law as law
import lexios.matter
from lexios.symbolic.symbol import Symbol
from lexios.typing import TimeType
from lexios.unit import Unit
from lexios.utils import camel_to_snake


class PropertyData(dict): pass
class _BaseProperty:
    def __init__(self):
        self.abrv: str | None = None
        self.unit: Unit | None = None
        self._data: PropertyData = PropertyData()
        self._laws: dict[str, law.Law] = dict()
        self._matter: lexios.matter.Matter | None = None

    @classmethod
    def class_name(cls) -> str:
        return camel_to_snake(cls.__name__)

    def symbol(self, t: int | float | tuple) -> Symbol | int | float:
        """Return a symbolic expression of this property"""
        assert isinstance(t, (tuple, float, tuple)), f"Expected {t} to be an integer, float or tuple (eg: (1, 2)) but got {type(t)}"
        assert isinstance(t[0], (int, float))
        assert isinstance(t[1], (int, float))

        if isinstance(t, (int, float)):
            expr = f"{self.abrv}_{t}"
        elif isinstance(t, tuple):
            assert len(t) == 2, "Expected 2 arguments, one for start time and one for end time"
            expr = fr'\Delta {self.abrv}_{t[0]},{t[1]}'

        symbol = Symbol(expr)
        symbol.set_state('t', t)
        symbol.set_state('name', self.class_name())
        symbol.set_state('type', 'prop')
        symbol.set_state('matter', self.matter)

        return symbol

    def get_val(self, t: TimeType) -> int | Symbol:
        """Get a value at a given time

        Args:
            t (int): time
        """
        return self._data[t]['val'] if t in self._data else self.symbol(t)

    def set_val(self, val: str | int, t: TimeType):
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
    def matter(self) -> lexios.matter.Matter | None:
        """An property can't exists without matter."""
        return self._matter

    @matter.setter
    def matter(self, matter: lexios.matter.Matter):
        assert issubclass(type(matter), lexios.matter.Matter), f"Expected matter to be a Matter, but got {type(matter)}"
        self._matter = matter

    def __call__(self, t: TimeType, **kwargs):
        kwargs = kwargs
        if 'eval' in kwargs and kwargs['eval'] == True:
            return self.get_val(t)
        else:
            return self.symbol(t)

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

    def __getitem__(self, k):
        if k in self.props:
            return self.props[k]
        super().__getitem__(k)

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
    assert issubclass(matter, lexios.matter.Matter) == True

    p = prop()
    p.add_law(law)
    p.matter(matter)
