from lexios.unit import Unit, str2unit
import lexios.unit as unit

import pytest
import sympy.physics.units as u

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (Unit.MASS, u.mass),
        (Unit.FORCE, u.force),
        (Unit.TIME, u.time)
    ]
)
@pytest.mark.xfail
def test_unit(test_input, expected):
    assert test_input == expected

@pytest.mark.xfail
def test_mass_unit():
    assert Unit.MASS == u.mass

@pytest.mark.parametrize(
    "test_input, expected",
    [
        ('10 kg', 10 * Unit.MASS),
        ('10 kilogram', 10 * Unit.MASS),
        ('10.2 kiLoGram', 10 * Unit.MASS)
    ]
)
def test_str2unit(test_input, expected):
    # TODO: implement
    assert str2unit(test_input) == expected

@pytest.mark.parametrize(
    "test_input, target_unit, expected",
    [
        (1.1 * Unit.KILOGRAM, Unit.GRAM, 1100.0 * Unit.GRAM)
    ]
)
def test_convert_between_quantities(test_input, target_unit, expected):
    assert unit.convert_to(test_input, target_unit) == expected