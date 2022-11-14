import pytest
from lexios.symbolic import symbol

@pytest.fixture
def mole():
    return symbol.Symbol('n')

def test_create_symbol(mole):
    assert str(mole) == 'n'
    assert mole.states == {}

def test_add_state_to_symbol(mole):
    mole.add_state('on_earth', True)
    assert mole.get_state('on_earth') == True

def test_get_state_that_not_exist(mole):
    # TODO: implement
    pass