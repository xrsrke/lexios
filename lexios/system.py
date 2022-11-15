from __future__ import annotations

from fastcore.meta import PrePostInitMeta


class _BaseSystem(metaclass=PrePostInitMeta):
    pass

class System(_BaseSystem):
    """A mediator object for communication between matter, properties and laws"""

    def get_prop(self, *args, **kwargs):
        pass
