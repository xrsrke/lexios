from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from lexios.core.law import Law
    from lexios.core.property import Property


class _BaseUniverse:
    def __init__(self):
        self._props: dict[str, Property] | None = {}
        self._laws: dict[str, Law] | None = {}

    @property
    def props(self) -> dict[str, Property] | None:
        return self._props

    @property
    def laws(self) -> dict[str, Law] | None:
        return self._laws


class Universe(_BaseUniverse): pass
