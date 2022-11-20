"""Implementation of Matter class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, NewType, Optional, TypedDict, Union

from fastcore.meta import PrePostInitMeta

import lexios.core.law
import lexios.core.property
import lexios.universe
from lexios.system import System
from lexios.typing import TypingPropertyValue, TypingTime

TypingUniverse = lexios.universe.Universe
TypingLaw = lexios.core.law.Law
TypingLawList = lexios.core.law.LawList
TypingProperty = lexios.core.property.Property


class PropertyInfo(TypedDict):
    """An object that store data of an property."""

    pass


class _BaseMatter(metaclass=PrePostInitMeta):
    """A generic class for matter."""

    def __init__(self):
        """Initialize a matter."""
        self._props: Dict[str, TypingProperty] = dict()
        self._laws: Dict[str, TypingLaw] = dict()
        self._universe: Optional[TypingUniverse] = None
        self._system: System = System()

    # def __post_init__(self):
    #     """Automatically initialize and add laws, properties to this matter"""
    #     self._init_laws()

    # def _init_laws(self):
    #     """Initialize and add laws, properties to this"""
    #     if self.laws:
    #         for law in self.laws:
    #             self.add_law(law)

    @property
    def laws(self) -> Dict[str, TypingLaw]:
        """Return the list of laws that this matter obeys to.

        Returns:
            _type_: _description_
        """
        return self._laws

    @laws.setter
    def laws(self, laws: List[TypingLaw]):
        """Add a list of laws to this matter."""
        # if isinstance(laws, TypingLawList):
        #     self._laws = laws.laws
        if isinstance(laws, TypingLawList):
            law_list = laws
            for name, law_class in law_list.laws.items():
                self.add_law(law_class)

    def add_law(self, law: TypingLaw):
        """Add a law class to this matter.

        Args:
            law (Law): A law
        """
        MatterCreator.add_law_to_matter(law, matter=self)

    @property
    def props(self) -> Dict[str, TypingProperty]:
        """Return the list of properties."""
        return self._props

    def add_prop(self, prop: TypingProperty):
        """Add a property to matter.

        Args:
            prop (Property): property
        """
        MatterCreator.add_prop_to_matter(prop, matter=self)

    def get_prop(self, name: str, t: TypingTime, **kwargs):
        """Get property value.

        Args:
            name (str): name of the property
            t (int): time

        Returns:
            _type_: _description_
        """
        return self.system.get_prop(name, t, instance=self, **kwargs)

    def set_prop(self, name: str, val: TypingPropertyValue, t: TypingTime, **kwargs):
        """Set value for an property."""
        return self.system.set_prop(name, val, t, instance=self, **kwargs)

    @property
    def universe(self) -> Optional[TypingUniverse]:
        """Return the universe that this matter belongs to.

        Returns:
            Optional[Universe]: the universe
        """
        return self._universe

    def set_universe(self, universe: TypingUniverse):
        """Set the universe which this matter belongs to."""
        assert isinstance(universe, TypingUniverse), f"Expected universe to be a Universe, got {type(universe)}"
        self._universe = universe

    @property
    def system(self) -> System:
        """Return the system."""
        return self._system

    @system.setter
    def system(self, system: System):
        """Set the system."""
        assert isinstance(system, System), f"Expected system to be a System, but got {type(system)}"
        self._system = system


class Matter(_BaseMatter):
    """A base class for derived different type of matters."""

    pass


class MacroMatter(Matter):
    """At macroscopic scale, matter behaves in different ways according to classical mechanics."""

    pass


class NanoMatter(_BaseMatter):
    """At nanoscale, matter behaves in different ways according to quantum mechanics."""

    pass


# def create_law_belongs_to_matter(law, matter):
#     assert issubclass(law, TypingLaw) == True
#     assert isinstance(matter, Matter) == True

#     l = law()
#     l.matter = matter
#     return l


class MatterCreator:
    """A class responsible for initialize all properties, laws belongs to a matter."""

    # def __init__(self, laws: TypingLawList, matter: Matter):
    #     self.laws = laws
    #     self.matter = matter

    @classmethod
    def add_laws_to_matter(cls, laws: TypingLawList, matter: Matter):
        """Add all the laws to matter."""
        for law in laws:
            law.matter = matter
            # matter.add_properties_in_law_to_matter()
            # matter.add_law()

    # def create_instance_from_class(self):
    #     pass

    @classmethod
    def add_law_to_matter(cls, law, matter):
        """Add a law to matter."""
        # assert issubclass(law, TypingLaw), f"Expected law to be a Law, got {type(law)}"

        name = law.class_name()
        if name not in matter.laws:
            law_instance = law if isinstance(law, TypingLaw) else law()
            # TODO: do't call ._matter directly
            law_instance._matter = matter
            matter.laws[name] = law_instance

            for name, prop in law_instance.props.items():
                MatterCreator.add_prop_to_matter(prop, matter)

    # @classmethod
    # def add_properties_in_law_to_matter(self, law):
    #     """Add all the properties in a law to matter."""
    #     for prop in law.properties:
    #         if prop.class_name not in self.matter.props:
    #             self.matter.add_prop(prop)

    @classmethod
    def add_prop_to_matter(cls, prop, matter):
        """Add a property to matter."""
        # assert issubclass(type(prop), TypingProperty), f"Expected property to be a Property, but got {type(prop)}"

        name = prop.class_name()
        if name not in matter.props:
            prop_instance = prop if isinstance(prop, TypingProperty) else prop()
            # TODO: all the logic in this function should be replace by prop.matter = matter
            prop_instance.matter = matter
            matter.props[name] = prop_instance

    # def initialize_law(self):
    #     pass
