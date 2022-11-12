from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)


if TYPE_CHECKING:
    from lexios.core.law import Law


class _BaseUniverse:
    def __init__(self):
        self._laws: Optional[Dict[str, Law]] = None
    
    @property
    def laws(self) -> Optional[Dict[str, Law]]:
        return self._laws


class Universe(_BaseUniverse): pass


class OurUniverse(Universe): pass