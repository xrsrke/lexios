from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
    List,
    TypedDict
)

from fastcore.meta import PrePostInitMeta

import lexios.core.law
import lexios.universe as universe
from lexios.core.property import Property
class PropertyInfo(TypedDict):
    pass

class _BaseMatter(metaclass=PrePostInitMeta):
    """A generic class for matter"""
    def __init__(self):
        self._props: Dict[str, Property] = dict()
        self._laws: Dict[str, lexios.core.law.Law] = dict()
        self._universe: Optional[universe.Universe] = None
    
    # def __post_init__(self):
    #     """Automatically initialize and add laws, properties to this matter"""
    #     self._init_laws()
    
    # def _init_laws(self):
    #     """Initialize and add laws, properties to this"""
    #     if self.laws:
    #         for law in self.laws:
    #             self.add_law(law)
    
    @property
    def laws(self) -> Dict[str, lexios.core.law.Law]:
        """Return the list of laws that this matter obeys to

        Returns:
            _type_: _description_
        """
        return self._laws

    @laws.setter
    def laws(self, laws: List[lexios.core.law.Law]):
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
        assert issubclass(law, lexios.core.law.Law), f"Expected law to be a Law, got {type(law)}"
        name = law.class_name()
        if not name in self.laws:
            self.laws[name] = create_law_belongs_to_matter(law=law, matter=self)
    
    @property
    def props(self) -> Dict[str, Property]:
        """Return the list of properties"""
        return self._props
    
    def add_prop(self, prop: Property):
        """Add a property to matter

        Args:
            prop (Property): property
        """
        assert isinstance(prop, Property), f"Expected property to be a Property, but got {type(prop)}"
        name = prop.class_name()
        if not name in self.props:
            self.props[name] = prop
    
    @property
    def universe(self) -> Optional[universe.Universe]:
        """Return the universe that this matter belongs to

        Returns:
            Optional[Universe]: the universe
        """
        return self._universe
    
    def set_universe(self, value: universe.Universe):
        assert isinstance(value, universe.Universe), f"Expected universe to be a Universe, got {type(universe)}"
        self._universe = value


class Matter(_BaseMatter): pass


class MarcoMatter(Matter):
    """At macroscopic scale, matter behaves in different ways according to classical mechanics"""
    pass

class NanoMatter(_BaseMatter):
    """At nanoscale, matter behaves in different ways accoriding to quantum mechanics"""
    pass


def create_law_belongs_to_matter(law, matter):
    assert issubclass(law, lexios.core.law.Law) == True
    assert isinstance(matter, Matter) == True
    
    l = law()
    l.matter = matter
    return l