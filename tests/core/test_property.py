import pytest
import lexios.core.property as prop
from lexios.unit import Unit

@pytest.fixture
def mass():
    return prop.Mass()

def test_create_empty_mass_property(mass):
    assert mass.abrv == 'm'
    assert repr(mass) == 'Mass'
    assert mass.unit == Unit.MASS
    assert mass.matter == None
    assert mass.laws == {}

def test_set_val_for_property(mass):
    mass.set_val('10 kg', t=2)
    mass.set_val(12.2 * Unit.MASS, t=3)
    
    mass.get_val(t=2) == Unit.MASS
    mass.get_val(t=3) == 12.2 * Unit.MASS
    
@pytest.mark.skip(reason="Will implement str2unit later")
def test_raise_exception_when_set_val_for_property(mass):
    with pytest.raises(ValueError, contains="Value need to be integer follows by unit"):
        mass.set_val('example')
    
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

# FOR TOTAL PROPERTY

@pytest.fixture
def force():
    force = prop.Force()
    force.add_value('1.1 ')

def test_return_symbolic_total_property():
    pass

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

def test_create_empty_property_list(empty_proplist):
    assert len(empty_proplist) == 0
    assert len(list(iter(empty_proplist))) == 0