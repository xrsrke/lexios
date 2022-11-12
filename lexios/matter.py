from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

from fastcore.meta import PrePostInitMeta

import lexios.core.law as law
import lexios.universe as universe
from lexios.core.property import Property
    

class _BaseMatter(metaclass=PrePostInitMeta):
    """A generic class for matter"""
    def __init__(self):
        self._props: Dict[str, Property] = dict()
        self._laws: Dict[str, law.Law] = dict()
        self._universe: Optional[universe.Universe] = None
    
    @property
    def laws(self) -> Dict[str, law.Law]:
        """Return the list of laws that this matter obeys to

        Returns:
            _type_: _description_
        """
        return self._laws
    
    def add_law(self, law: law.Law):
        """Add law to this matter

        Args:
            law (Law): A law
        """
        assert isinstance(law, law.Law), f"Expected law to be a Law, got {type(law)}"
        name = law.class_name()
        if not name in self.laws:
            self.laws[name] = law
    
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