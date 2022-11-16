from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Any, Dict, List, NoReturn, Optional

import lexios.core.property as prop
import lexios.matter
from lexios.utils import camel_to_snake

if TYPE_CHECKING:
    from lexios.core.property import Property


class _BaseLaw(ABC):
    """A law is an abstract concept. It can independenly exists without having matter"""

    def __init__(self, matter: lexios.matter.Matter | None = None) -> None:
        """Initialize a new law

        Args:
            matter (Optional[lexios.matter.Matter], optional): matter that this law belongs to. Defaults to None.
        """
        self._props: dict[str, Property] = dict()
        # self._matter: Optional[lexios.matter.Matter] = None
        self.matter = matter

    @property
    def props(self) -> dict[str, Property]:
        """Return a dictionary of properties that belong this law

        Returns:
            Dict[str, Property]: a dictionary of properties
        """
        return self._props

    @props.setter
    def props(self, props: dict):
        """Set a list of properties that belong to this law"""
        if isinstance(props, prop.PropList):
            for name, property in iter(props):
                self.add_prop(name, property)

            # if self.matter:
            #     self.add_law_to_matter(self.matter)

    def get_prop(self, name: str) -> Property | None:
        """Return the property of this law"""
        assert isinstance(name, str), f"Expected str to be a string, got {type(name)}"
        name = name.lower()

        for prop in self.props:
            if prop['prop'].class_name() == name:
                return prop

    def add_prop(self, name: str, prop: prop.Property):
        self._props[name] = prop

    def add_props_to_matter(self, matter: lexios.matter.Matter):
        """Add all properties that belongs to this law to the matter

        Args:
            matter (_type_): Matter
        """

        assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"

        if not self.props:
            for prop in self.props:
                matter.add_prop(prop)

    def add_law_to_matter(self, matter: lexios.matter.Matter):
        """Add this law to the matter

        Args:
            matter (_type_): Matter
        """
        assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be Matter, got {type(matter)}"
        matter.add_law(self)
        self.add_props_to_matter(matter)

    @property
    def matter(self) -> lexios.matter.Matter | None:
        return self._matter

    @matter.setter
    def matter(self, matter: lexios.matter.Matter | None):
        """Set which matter this law belongs to"""
        # assert isinstance(matter, (lexios.matter.Matter, None)), f"Expected matter to be a Matter, got {type(matter)}"
        self._matter = matter
        # self.add_law_to_matter(matter)
        # TODO: If a law belongs to some matter => move properties to that matter

    @classmethod
    def class_name(cls) -> str:  # return the snake style name
        return camel_to_snake(cls.__name__)

    @abstractclassmethod
    def expr(self):
        """The relations between properties

        Raises:
            NotImplemented: _description_
        """
        raise NotImplemented(f"expr not implemented for {type(self)}")


class Law(_BaseLaw):
    """Base class for all laws in matter"""
    pass

class LawList:
    """Holds all laws in a list"""
    def __init__(self, laws: list[Law] = None):
        self._laws: dict[str, Law] = {}

        if laws is not None:
            for law in laws:
                name = law.class_name()
                self._laws[name] = law

    @property
    def laws(self) -> dict[str, Law]:
        return self._laws

    def __len__(self):
        return len(self.laws)

    def __iter__(self):
        return iter(self.laws.items())
