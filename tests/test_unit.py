from lexios.unit import Unit

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