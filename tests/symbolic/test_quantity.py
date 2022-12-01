from __future__ import annotations

import pytest

from lexios.symbolic.quantity import Quantity
from lexios.unit import Unit


@pytest.fixture
def ten_kg():
    return Quantity(10 * Unit.KILOGRAM)


@pytest.fixture
def five_kg():
    return Quantity(5 * Unit.KILOGRAM)


@pytest.fixture
def fifteen_kg():
    return Quantity(15 * Unit.KILOGRAM)


@pytest.mark.skip
def test_create_quantity(ten_kg):
    assert ten_kg() == 10 * Unit.KILOGRAM
    assert ten_kg.unit == Unit.KILOGRAM
    assert ten_kg.val == 10
    assert str(ten_kg) == "10*kilogram"


@pytest.mark.skip
def test_set_state_for_quantity(ten_kg):
    ten_kg.set_state("t", 2)

    assert ten_kg.get_state("t") == 2


@pytest.mark.skip
def test_add_quantity(ten_kg, five_kg, fifteen_kg):
    result = ten_kg + five_kg
    assert result == fifteen_kg
