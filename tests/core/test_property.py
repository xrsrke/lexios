from lexios.core.property import (
    Property,
    Mass,
    Mole
)
from lexios.unit import Unit

def test_mass():
    mass = Mass()
    assert mass.abrv == 'm'
    assert mass.unit == Unit.MASS
    assert mass.matter == None
    assert mass.laws == {}