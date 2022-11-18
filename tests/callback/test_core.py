from __future__ import annotations

import pytest

from lexios.callback.core import Callback
from lexios.unit import Unit


def test_create_callback(convert_to_pound_callback):
    assert convert_to_pound_callback().name == "convert_to_pound"


# @pytest.fixture
# def matter_with_law_and_callback(matter_with_law):
#     return matter_with_law.add_cb(ConvertToPoundCallback)


# def test_add_callback_to_matter(matter_with_law_and_callback):
#     assert len(matter_with_law_and_callback.cbs) == 1

#     matter_with_law_and_callback.set_prop("mass", 10 * Unit.KILOGRAM, t=1)
#     ten_kg_in_pound = 22.046 * Unit.POUND
#     assert matter_with_law_and_callback.get_prop("mass", t=1).eval() == ten_kg_in_pound


# def test_remove_callback_from_matter(matter_with_law_and_callback):
#     matter_with_law_and_callback.remove_cb(ConvertToPoundCallback)
#     assert len(matter_with_law_and_callback.cbs) == 0
