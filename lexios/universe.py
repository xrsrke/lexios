"""Universe."""

from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from lexios.core.law import Law
    from lexios.core.property import Property


class _BaseUniverse:
    """Base Universe."""

    def __init__(self):
        """Initialize."""
        self._props: Dict[str, Property] = {}
        self._laws: Dict[str, Law] = {}

    @property
    def props(self) -> Dict[str, Property]:
        """Return all the properties that belongs to the universe."""
        return self._props

    @property
    def laws(self) -> Dict[str, Law]:
        """Return all the laws that belongs to the universe."""
        return self._laws


class Universe(_BaseUniverse):
    """Universe."""

    pass
