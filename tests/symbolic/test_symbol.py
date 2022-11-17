from __future__ import annotations

import pytest

from lexios.symbolic.symbol import Symbol


@pytest.fixture
def mole():
    return Symbol('n')

def test_create_symbol(mole):
    assert str(mole) == 'n'
    assert mole.states == {}

def test_get_state_not_exist_from_symbol(mole):
    assert mole.get_state('non_exist') == None

def test_set_state_to_symbol(mole):
    mole.set_state('on_earth', True)
    assert mole.get_state('on_earth') == True
