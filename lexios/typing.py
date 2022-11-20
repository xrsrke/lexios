"""Common typing hints."""

from __future__ import annotations

from typing import NewType, Tuple, Union

TimeType = Union[int, float, tuple[Union[int, float]]]

Time = Union[int, float]
ChangeInTime = Tuple[Union[int, float]]
TypingTime = Union[Time, ChangeInTime]

PropertyValue = Union[int, float, bool]
TypingPropertyValue = NewType("lexios.core.property.PropertyValue", PropertyValue)
