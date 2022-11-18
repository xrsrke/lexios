from __future__ import annotations

import pytest

import lexios.core.property as prop
from lexios.symbolic.symbol import Symbol
from lexios.unit import Unit


@pytest.fixture
def force_with_value():
    force = prop.Force()
    force.set_val(10 * Unit.NEWTON, t=1)
    force.set_val(30 * Unit.NEWTON, t=2)
    return force


def test_create_empty_mass_property(mass):
    assert mass.abrv == "m"
    assert repr(mass) == "Mass"
    assert mass.unit == Unit.MASS
    assert mass.matter is None
    assert mass.laws == {}
    assert isinstance(mass.symbol(t=3), Symbol)
    assert isinstance(mass(t=3), Symbol)


def test_set_val_for_property(mass):
    mass.set_val("10 kg", t=2)
    mass.set_val(12.2 * Unit.MASS, t=3)

    mass.get_val(t=2) == Unit.MASS
    mass.get_val(t=3) == 12.2 * Unit.MASS


def test_eval_nonempty_property(force_with_value):
    assert force_with_value(t=1).eval() == 10 * Unit.NEWTON


@pytest.mark.skip(reason="Will implement str2unit later")
def test_raise_exception_when_set_val_for_property(mass):
    with pytest.raises(ValueError, contains="Value need to be integer follows by unit"):
        mass.set_val("example")

    with pytest.raises(ValueError, contains="Need to specify time"):
        mass.set_val("10 kg")

    with pytest.raises(ValueError, contains="Time need to be an positive integer"):
        mass.set_val("10 kg", t=-1)


def test_get_value_that_not_exist_for_property():
    pass


def test_remove_value_that_not_exist_for_property():
    pass


def test_add_get_remove_value_for_property():
    pass


################################################################
# FOR TOTAL PROPERTY


def test_create_empty_symbolic_total_property(mass):
    assert isinstance(mass(t=(1, 2)), Symbol)
    assert isinstance(mass(t=(1, 2), eval=True), Symbol)


def test_create_nonempty_symbolic_total_property(force_with_value):
    assert isinstance(force_with_value(t=(1, 2)), Symbol)

    assert force_with_value(t=(1, 2), eval=True) == 20 * Unit.NEWTON
    assert force_with_value.get_val(t=(2, 1), eval=True) == 20 * Unit.NEWTON

    # assert force_with_value(t=(1, 2)).get_state('t_start') == 1
    # assert force_with_value(t=(1, 2)).get_state('t_end') == 2


################################################################
# FOR PROPERTY LIST


@pytest.fixture
def proplist():
    props = [prop.Force, prop.Mass, prop.Acceleration]
    return prop.PropList(props)


@pytest.fixture
def empty_proplist():
    return prop.PropList()


def test_create_property_list(proplist):
    assert len(proplist) == 3
    assert len(list(iter(proplist))) == 3
    assert len(proplist.props) == 3
    assert issubclass(proplist["force"], prop.Force)


def test_create_empty_property_list(empty_proplist):
    assert len(empty_proplist) == 0
    assert len(list(iter(empty_proplist))) == 0
