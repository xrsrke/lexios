"""System."""

from __future__ import annotations

from typing import Union

from fastcore.meta import PrePostInitMeta

import lexios.core.law as law
import lexios.matter as matter
from lexios.typing import TypingTime


class _BaseSystem(metaclass=PrePostInitMeta):
    """System."""

    pass


class System(_BaseSystem):
    """A mediator object for communication between matter, properties and laws."""

    def __init__(self):
        """Initialize."""
        self._states = {"x": 1}

    def get_prop(
        self,
        name: str,
        t: TypingTime,
        instance: Union[matter.Matter, law.Law],
        **kwargs,
    ):
        """Get properties."""
        if isinstance(instance, matter.Matter):
            return instance.props[name](t, **kwargs)

    def set_prop(self, name: str, val, t: TypingTime, instance, **kwargs):
        """Set the properties."""
        if isinstance(instance, matter.Matter):
            instance.props[name].set_val(val, t, **kwargs)
