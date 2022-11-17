from __future__ import annotations

from typing import Union

from fastcore.meta import PrePostInitMeta

import lexios.core.law as law
import lexios.matter as matter


class _BaseSystem(metaclass=PrePostInitMeta):
    pass

class System(_BaseSystem):
    """A mediator object for communication between matter, properties and laws"""
    def __init__(self):
        self._states = {'x': 1}

    def get_prop(self, name: str, t: int, instance: matter.Matter | law.Law, **kwargs):
        if isinstance(instance, matter.Matter):
            return instance.props[name](t, **kwargs)

    def set_prop(self, name: str, val, t: int, instance, **kwargs):
        if isinstance(instance, matter.Matter):
            instance.props[name].set_val(val, t, **kwargs)
