"""Implementation of Law class."""

from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Dict, List, Optional

from fastcore.foundation import L

import lexios.core.property as prop
import lexios.matter
from lexios.callback.core import Callback
from lexios.utils import camel_to_snake

if TYPE_CHECKING:
    from lexios.core.property import Property

# lexios.core.property.PropList = lexios.core.property.PropList
# lexios.matter.Matter = lexios.matter.Matter


class _BaseLaw(ABC):
    """A law is an abstract concept. It can independenly exists without having matter."""

    def __init__(self, matter: Optional[lexios.matter.Matter] = None, cbs: Optional[List[Callback]] = []):
        """Initialize a new law.

        Args:
            matter (Optional[lexios.matter.Matter], optional): matter that this law belongs to. Defaults to None.
            cbs: a list of callbacks
        """
        self._props: Dict[str, Property] = dict()
        self._matter: Optional[lexios.matter.Matter] = None
        self.matter = matter
        self.cbs = L([])
        self.add_cbs(cbs)

    @property
    def props(self) -> Dict[str, Property]:
        """Return a dictionary of properties that belong this law.

        Returns:
            Dict[str, Property]: a dictionary of properties
        """
        return self._props

    @props.setter
    def props(self, props: lexios.core.property.PropList):
        """Set a list of properties that belong to this law."""
        if isinstance(props, lexios.core.property.PropList):
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

    # def add_props_to_matter(self, matter: lexios.matter.Matter):
    #     """Add all properties that belongs to this law to the matter."""
    #     assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be a Matter, got {type(matter)}"

    #     if not self.props:
    #         for prop in self.props:
    #             matter.add_prop(prop)

    # def add_law_to_matter(self, matter: lexios.matter.Matter):
    #     """Add this law to the matter.

    #     Args:
    #         matter (_type_): Matter
    #     """
    #     assert isinstance(matter, lexios.matter.Matter), f"Expected matter to be Matter, got {type(matter)}"
    #     # LawCreator(self).add_to_matter(matter)
    #     # matter.add_law(self)
    #     # self.add_props_to_matter(matter)

    def ordered_cbs(self) -> List[Callback]:
        # if len(self.cbs > 0):
        return [cb for cb in self.cbs.sorted("order")]

    def add_cbs(self, cbs: List[Callback]):
        """Add a list of callbacks.

        Args:
            cbs (List[Callback]): a list of callbacks
        """
        L(cbs).map(self.add_cb)

    def add_cb(self, cb: Callback):
        if isinstance(cb, type):
            cb = cb()
        cb.law = self
        self.cbs.append(cb)

    def remove_cb(self, cb: Callback):
        """Remove a callback from the list of callback.

        Args:
            cb (Callback): callback you want to remove
        """
        cb.law = None
        if cb in self.cbs:
            self.cbs.remove(cb)

    @property
    def matter(self) -> Optional[lexios.matter.Matter]:
        return self._matter

    @matter.setter
    def matter(self, matter: Optional[lexios.matter.Matter]):
        """Set which matter this law belongs to."""
        # assert isinstance(matter, (lexios.matter.Matter, None)), f"Expected matter to be a Matter, got {type(matter)}"
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


class LawCreator:
    """Responsible for create a law belongs to a matter."""

    def __init__(self, law: Law):
        """Initialize."""
        self.law = law

    def add_props_to_matter(self, matter):
        """Add all properties belongs to this law to matter."""
        if not self.law.props:
            for p in self.law.props:
                matter.add_prop(p)

    def add_to_matter(self, matter: lexios.matter.Matter):
        """Add the law to matter."""
        matter.add_law(self)
        self.add_props_to_matter(matter)


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
