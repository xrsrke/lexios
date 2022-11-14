import pytest

from lexios.matter import Matter, MacroMatter
import lexios.core.law as law
import lexios.core.property as prop
from lexios.universe import Universe
from lexios.unit import Unit
from lexios.physics.newton import NewtonFirstLaw, NewtonSecondLaw

def test_create_law_for_an_matter():
    pass

@pytest.mark.parametrize(
    "matter",
    [
        (Matter()), # create matter without universe
        (Matter(universe=Universe())) # create matter with universe
    ]
)
def test_create_matter_using_matter_class(matter):
    assert matter.props == {}
    assert matter.laws == {}
    assert matter.universe == None

class Star(MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = law.LawList([NewtonFirstLaw])

class Earth(MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = [NewtonFirstLaw]
        for law in self.laws:
            name = law.class_name()
            self.add_law(name, law)
            
@pytest.fixture
def star():
    return Star()

@pytest.fixture
def earth():
    return Earth()

@pytest.mark.xfail
@pytest.mark.parametrize('matter', [earth(), star()])
def test_create_customize_macro_matter(matter):
    
    # not implemented
    assert matter.get_law('newton_first_law') == NewtonFirstLaw
    assert len(matter.laws) == 1
    assert matter.get_prop('mass') == prop.Mass
    assert len(matter.props) == 3

@pytest.mark.xfail
def test_add_law_to_matter(star):
    # not implemented
    star.add_law(NewtonSecondLaw)
    assert len(star.laws)

@pytest.mark.xfail
def test_remove_law_from_matter(star):
    # not implemented
    star.remove_law(NewtonFirstLaw)
    assert len(star.laws) == 0
    assert len(star.props) == 0

@pytest.mark.xfail
def test_set_get_remove_value_for_property_in_matter(star):
    # not implemented
    
    # add value
    values = [1, 1.5, 3.5]
    for value, time in list(zip(values, range(1, 4))):
        star.set_value('mass', value=(value * Unit.MASS), t=time)
    
    # get value
    assert star.get_prop('mass', t=1) == (1 * Unit.MASS)
    assert star.get_prop('mass', t=2) == (1.5 * Unit.MASS)
    assert star.get_prop('mass', t=3) == (3.5 * Unit.MASS)
    
    # remove value
    star.remove_value(t=1)
    star.remove_value(t=3)
    assert star.get_prop('mass', t=1) == None
    assert star.get_prop('mass', t=2) == (1.5 * Unit.MASS)
    assert star.get_prop('mass', t=3) == None

def test_symbolic_sum_of_properties():
    pass