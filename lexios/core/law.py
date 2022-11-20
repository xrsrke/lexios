"""Implementation of Law class."""

from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Any, Dict, List, Optional

import lexios.core.property as prop
import lexios.matter
from lexios.callback.core import Callback
from lexios.utils import camel_to_snake

if TYPE_CHECKING:
    from lexios.core.property import Property

TypingPropList = lexios.core.property.PropList
TypingMatter = lexios.matter.Matter


class _BaseLaw(ABC):
    """A law is an abstract concept. It can independenly exists without having matter."""

    def __init__(self, matter: Optional[TypingMatter] = None):
        """Initialize a new law.

        Args:
            matter (Optional[TypingMatter], optional): matter that this law belongs to. Defaults to None.
        """
        self._props: Dict[str, Property] = dict()
        # self._matter: Optional[TypingMatter] = None
        self.matter = matter
        self.cbs: List[Callback] = []

    @property
    def props(self) -> Dict[str, Property]:
        """Return a dictionary of properties that belong this law.

        Returns:
            Dict[str, Property]: a dictionary of properties
        """
        return self._props

    @props.setter
    def props(self, props: TypingPropList):
        """Set a list of properties that belong to this law."""
        if isinstance(props, prop.PropList):
            for name, prop in iter(props):
                self.add_prop(name, prop)

    def get_prop(self, name: str) -> Optional[Property]:
        """Return the property of this law."""
        assert isinstance(name, str), f"Expected str to be a string, got {type(name)}"
        name = name.lower()

        for prop in self.props:
            if prop["prop"].class_name() == name:
                return prop

        return None

    def add_prop(self, name: str, prop: prop.Property):
        """Add a property.

        Args:
            name (str): name of the property
            prop (prop.Property): the class of the property
        """
        self._props[name] = prop

    def add_props_to_matter(self, matter: TypingMatter):
        """Add all properties that belongs to this law to the matter."""
        assert isinstance(matter, TypingMatter), f"Expected matter to be a Matter, got {type(matter)}"

        if not self.props:
            for prop in self.props:
                matter.add_prop(prop)

    def add_law_to_matter(self, matter: TypingMatter):
        """Add this law to the matter.

        Args:
            matter (_type_): Matter
        """
        assert isinstance(matter, TypingMatter), f"Expected matter to be Matter, got {type(matter)}"
        matter.add_law(self)
        self.add_props_to_matter(matter)

    def add_cbs(self, cbs: List[Callback]):
        """Add a list of callbacks.

        Args:
            cbs (List[Callback]): a list of callbacks
        """
        for cb in cbs:
            self.add_cb(cb)

    def add_cb(self, cb: Callback):
        if isinstance(cb, type):
            cb = cb()
        cb.law = self
        self.cbs.append(cb)

    # def _with_events(self):
    #     pass

    @property
    def matter(self) -> Optional[TypingMatter]:
        return self._matter

    @matter.setter
    def matter(self, matter: Optional[TypingMatter]):
        """Set which matter this law belongs to."""
        # assert isinstance(matter, (TypingMatter, None)), f"Expected matter to be a Matter, got {type(matter)}"
        self._matter = matter
        # self.add_law_to_matter(matter)
        # TODO: If a law belongs to some matter => move properties to that matter

    @classmethod
    def class_name(cls) -> str:  # return the snake style name
        return camel_to_snake(cls.__name__)

    @abstractclassmethod
    def expr(self):
        """The relations between properties.

        Raises:
            NotImplemented: _description_
        """
        raise NotImplemented(f"expr not implemented for {type(self)}")


class Law(_BaseLaw):
    """Base class for all laws in matter."""

    pass


class LawList:
    """Holds all laws in a list."""

    def __init__(self, laws: Optional[List[Law]] = None):
        """Initialize a law list."""
        self._laws: Dict[str, Law] = {}

        if laws is not None:
            for law in laws:
                name = law.class_name()
                self._laws[name] = law

    @property
    def laws(self) -> Dict[str, Law]:
        """Return a list of laws."""
        return self._laws

    def __len__(self):
        """Return the number of laws."""
        return len(self.laws)

    def __iter__(self):
        """Return an iterator of laws."""
        return iter(self.laws.items())
