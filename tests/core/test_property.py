import pytest
from lexios.core.property import (
    Property,
    Mass,
    Mole,
    Force
)
from lexios.unit import Unit

def test_create_empty_mass_property():
    mass = Mass()
    assert mass.abrv == 'm'
    assert mass.unit == Unit.MASS
    assert mass.matter == None
    assert mass.laws == {}

def add_value_that_already_exist_for_property():
    pass

def get_value_that_not_exist_for_property():
    pass

def remove_value_that_not_exist_for_property():
    pass

def test_add_get_remove_value_for_property():
    pass

# FOR TOTAL PROPERTY

@pytest.fixture
def force():
    force = Force()
    force.add_value('1.1 ')

def test_return_symbolic_total_property():
    pass