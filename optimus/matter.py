from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
    NoReturn
)

from fastcore.meta import PrePostInitMeta

import optimus.core.law as law
from optimus.core.property import Property

if TYPE_CHECKING:
    from optimus.universe import Universe
    

class _BaseMatter(metaclass=PrePostInitMeta):
    """A generic class for matter"""
    def __init__(self):
        self._props: Dict[str, Property] = dict()
        self._laws: Dict[str, law.Law] = dict()
        self._universe: Optional[Universe] = None
    
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
        """Add a property to the law

        Args:
            prop (Property): property
        """
        assert isinstance(prop, Property), f"Expected property to be a Property, but got {type(prop)}"
        name = prop.class_name()
        if not name in self.props:
            self.props[name] = prop
    
    @property
    def universe(self) -> Optional[Universe]:
        """Return the universe that this matter belongs to

        Returns:
            Optional[Universe]: the universe
        """
        return self._universe
    
    def set_universe(self, universe: Universe):
        assert isinstance(universe, Universe), f"Expected universe to be a Universe, got {type(universe)}"
        self._universe = universe


class Matter(_BaseMatter): pass