"""Implementation of Property class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Union

import lexios.core.law
import lexios.matter
from lexios.symbolic.symbol import Symbol
from lexios.typing import TypingPropertyValue, TypingTime
from lexios.unit import Unit
from lexios.utils import camel_to_snake

TypingLaw = lexios.core.law.Law


class PropertyData(dict):
    """Store data of property."""

    pass


class _BaseProperty:
    def __init__(self):
        """Initialize property."""
        self.abrv: str | None = None
        self.unit: Unit | None = None
        self._data: PropertyData = PropertyData()
        self._laws: Dict[str, TypingLaw] = dict()
        self._matter: Optional[lexios.matter.Matter] = None

    @classmethod
    def class_name(cls) -> str:
        """Return the snake style name of class."""
        return camel_to_snake(cls.__name__)

    def symbol(self, t: TypingTime) -> Union[Symbol, TypingPropertyValue]:
        """Return a symbolic expression of this property."""
        assert isinstance(
            t, (int, float, tuple)
        ), f"Expected t to be an integer, float or tuple (eg: (1, 2)) but got {type(t)}"

        if isinstance(t, (int, float)):
            expr = f"{self.abrv}_{t}"
        elif isinstance(t, tuple):
            assert isinstance(t[0], (int, float))
            assert isinstance(t[1], (int, float))
            assert len(t) == 2, "Expected 2 arguments, one for start time and one for end time"
            expr = rf"\Delta {self.abrv}_{t[0]},{t[1]}"

        symbol = Symbol(expr)
        symbol.set_state("t", t)
        symbol.set_state("name", self.class_name())
        symbol.set_state("type", "prop")
        symbol.set_state("matter", self.matter)

        return symbol

    def get_val(self, t: TypingTime) -> Union[Symbol, TypingPropertyValue]:
        """Get a value at a given time.

        Args:
            t (int): time
        """
        return self._data[t]["val"] if t in self._data else self.symbol(t)

    def set_val(self, val: TypingPropertyValue, t: TypingTime):
        """Set the value at a given time for property.

        Args:
            val (Union[str, int]): value
            t (int): time
        """
        self._data[t] = {"val": val}

    @property
    def laws(self) -> Dict[str, TypingLaw]:
        """Return a list of laws that associated with this property."""
        return self._laws

    def add_law(self, law: TypingLaw):
        """Add a law that associated with this property."""
        assert isinstance(law, lexios.core.law.Law), f"Expected law to be a Law, got {type(law)}"

        name = law.class_name()
        if self._laws and name not in self._laws:
            self._laws[name] = law

    def remove_law(self, name: str):
        """Remove a law from this property.

        Docstring.remove_law(self, name: str
        """
        pass

    @property
    def matter(self) -> lexios.matter.Matter | None:
        """An property can't exists without matter."""
        return self._matter

    @matter.setter
    def matter(self, matter: lexios.matter.Matter):
        """Return the matter that this property belongs to."""
        assert issubclass(type(matter), lexios.matter.Matter), f"Expected matter to be a Matter, but got {type(matter)}"
        self._matter = matter

    def __call__(self, t: TypingTime, **kwargs):
        """Call."""
        kwargs = kwargs
        if "eval" in kwargs and kwargs["eval"] is True:
            return self.get_val(t)
        else:
            return self.symbol(t)

    def __repr__(self) -> str:
        """Return an expression of the class."""
        return f"{self.class_name().capitalize()}"


class Property(_BaseProperty):
    """Base class for all properties in matter."""

    pass


class PropList:
    """Holds all properties in a list."""

    def __init__(self, props: List[Property] = None):
        """Initialize a property list."""
        self._props: Dict[str, Property] = {}

        if props is not None:
            for prop in props:
                name = prop.class_name()
                self._props[name] = prop

    @property
    def props(self) -> Dict[str, Property]:
        """Return all properties of this property list."""
        return self._props

    def __getitem__(self, k):
        """Get an item in property list."""
        if k in self.props:
            return self.props[k]
        super().__getitem__(k)

    def __len__(self) -> int:
        """Return the number of properties."""
        return len(self.props)

    def __iter__(self) -> Iterable[str, Property]:
        """Return an iterable of properties."""
        return iter(self.props.items())


class Mass(Property):
    """Mass Property."""

    def __init__(self):
        """Initialize the Mass property."""
        super().__init__()
        self.abrv = "m"
        self.unit = Unit.MASS


class Mole(Property):
    """Mole Property."""

    def __init__(self):
        """Initialize the Mole property."""
        super().__init__()
        self.abrv = "n"
        self.unit = Unit.MOLE


class Force(Property):
    """Force Property."""

    def __init__(self):
        """Initialize the Force property."""
        super().__init__()
        self.abrv = "F"
        self.unit = Unit.FORCE


class Acceleration(Property):
    """Acceleration Property."""

    def __init__(self):
        """Initialize the Acceleration property."""
        super().__init__()
        self.abrv = "a"
        self.unit = Unit.ACCELERATION


# def create_property_belongs_to_matter(prop, law, matter):
#     assert isinstance(prop, Property)
#     assert isinstance(law, law.Law)
#     assert issubclass(matter, lexios.matter.Matter)

#     p = prop()
#     p.add_law(law)
#     p.matter(matter)


class Weight(Property):
    """Weight Property."""

    def __init__(self):
        """Initialize the Weight property."""
        super().__init__()
        self.abrv = "w"
        self.unit = Unit.NEWTON


class GravityAcceleration(Property):
    """Gravity acceleration property."""

    def __init__(self):
        """Initialize the Gravity acceleration property."""
        super().__init__()
        self.abrv = "g"
        self.unit = Unit.ACCELERATION
