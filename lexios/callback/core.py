"""Implementation of Callback class."""

from __future__ import annotations

from fastcore.basics import class2attr
from fastcore.foundation import L
from fastcore.meta import funcs_kwargs

_events = [
    "before_create_unv",
    "after_create_unv",
    "before_create_env",
    "after_create_env",
    "before_create_matter",
    "after_create_matter",
    "before_get_prop",
    "after_get_prop",
    "before_change_prop",
    "after_change_prop",
    "before_get_law",
    "after_get_law",
    "before_change_law",
    "after_change_law",
]


@funcs_kwargs(as_method=True)
class Callback:
    """A base class for create new callback."""

    _methods = _events

    def __repr__(self):
        """repr."""
        return type(self).__name__

    @property
    def name(self) -> str:
        """Name of the callback in camel style, with _callback removed."""
        return class2attr(self, "Callback")
