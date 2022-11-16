from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional, TypedDict, Union

from fastcore.meta import PrePostInitMeta

import lexios.core.law
import lexios.core.property
import lexios.universe as universe
from lexios.system import System


class PropertyInfo(TypedDict):
    pass

class _BaseMatter(metaclass=PrePostInitMeta):
    """A generic class for matter"""
    def __init__(self):
        self._props: dict[str, lexios.core.Property] = dict()
        self._laws: dict[str, lexios.core.law.Law] = dict()
        self._universe: universe.Universe | None = None
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
    def laws(self) -> dict[str, lexios.core.law.Law]:
        """Return the list of laws that this matter obeys to

        Returns:
            _type_: _description_
        """
        return self._laws

    @laws.setter
    def laws(self, laws: list[lexios.core.law.Law]):
        # if isinstance(laws, lexios.core.law.LawList):
        #     self._laws = laws.laws
        if isinstance(laws, lexios.core.law.LawList):
            law_list = laws
            for name, law_class in law_list.laws.items():
                self.add_law(law_class)

    def add_law(self, law: lexios.core.law.Law):
        """Add a law class to this matter

        Args:
            law (Law): A law
        """
        MatterCreator.add_law_to_matter(law, matter=self)

    @property
    def props(self) -> dict[str, lexios.core.property.Property]:
        """Return the list of properties"""
        return self._props

    def add_prop(self, prop: lexios.core.property.Property):
        """Add a property to matter

        Args:
            prop (Property): property
        """
        MatterCreator.add_prop_to_matter(prop, matter=self)

    def get_prop(self, *args, **kwargs):
        return self.system.get_prop(*args, **kwargs, instance=self)

    @property
    def universe(self) -> universe.Universe | None:
        """Return the universe that this matter belongs to

        Returns:
            Optional[Universe]: the universe
        """
        return self._universe

    def set_universe(self, value: universe.Universe):
        assert isinstance(value, universe.Universe), f"Expected universe to be a Universe, got {type(universe)}"
        self._universe = value

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, system: System):
        assert isinstance(system, System), f"Expected system to be a System, but got {type(system)}"
        self._system = system

class Matter(_BaseMatter): pass


class MacroMatter(Matter):
    """At macroscopic scale, matter behaves in different ways according to classical mechanics"""
    pass

class NanoMatter(_BaseMatter):
    """At nanoscale, matter behaves in different ways according to quantum mechanics"""
    pass


def create_law_belongs_to_matter(law, matter):
    assert issubclass(law, lexios.core.law.Law) == True
    assert isinstance(matter, Matter) == True

    l = law()
    l.matter = matter
    return l

class MatterCreator():
    # def __init__(self, laws: lexios.core.law.LawList, matter: Matter):
    #     self.laws = laws
    #     self.matter = matter

    @classmethod
    def add_laws_to_matter(cls, laws: lexios.core.law.Law, matter: Matter):
        """Add all the laws to matter."""
        for law in laws:
            law.matter = matter
            # matter.add_properties_in_law_to_matter()
            # matter.add_law()

    @classmethod
    def add_law_to_matter(cls, law, matter):
        # assert issubclass(law, lexios.core.law.Law), f"Expected law to be a Law, got {type(law)}"

        name = law.class_name()
        if not name in matter.laws:
            law_instance = law if isinstance(law, lexios.core.law.Law) else law()
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
        # assert issubclass(type(prop), lexios.core.property.Property), f"Expected property to be a Property, but got {type(prop)}"

        name = prop.class_name()
        if not name in matter.props:
            prop_instance = prop if isinstance(prop, lexios.core.property.Property) else prop()
            matter.props[name] = prop_instance

    # def initialize_law(self):
    #     pass
