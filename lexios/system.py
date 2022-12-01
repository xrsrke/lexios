"""System."""

from __future__ import annotations

from typing import Dict, TypeVar, Union

from fastcore.meta import PrePostInitMeta

import lexios.core.law as law
import lexios.core.property
import lexios.matter as matter
from lexios.typing import TypingTime

T = TypeVar("T")


class _BaseSystem(metaclass=PrePostInitMeta):
    """System."""

    pass


class System(_BaseSystem):
    """A mediator object for communication between matter, properties and laws."""

    def __init__(self):
        """Initialize."""
        self._states = {"x": 1}

    def set_state_to_prop(self, prop: lexios.core.property.Property, states: Dict[str, T]):
        """Set state to prop."""
        prop.set_states(states)

    def get_prop(
        self,
        name: str,
        t: TypingTime,
        instance: Union[matter.Matter, law.Law],
        **kwargs,
    ):
        """Get properties."""
        if isinstance(instance, matter.Matter):
            prop = instance.props[name]
            states = {"t": t, **kwargs}
            self.set_state_to_prop(prop, states)

            return prop(t, **kwargs)

    def set_prop(self, name: str, val, t: TypingTime, instance, **kwargs):
        """Set the properties."""
        if isinstance(instance, matter.Matter):
            prop = instance.props[name]
            states = {"val": val, "t": t, **kwargs}
            self.set_state_to_prop(prop, states)

            prop.set_val(val, t, **kwargs)
