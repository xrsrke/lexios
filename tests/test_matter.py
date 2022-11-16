from __future__ import annotations

import pytest

import lexios.core.law as law
import lexios.core.property as prop
from lexios.matter import MacroMatter, Matter
from lexios.physics.newton import NewtonFirstLaw
from lexios.system import System
from lexios.unit import Unit
from lexios.universe import Universe

################################################################
### TEST CREATE MATTER

def test_create_law_for_an_matter():
    pass

@pytest.mark.parametrize(
    "matter",
    [
        (Matter()), # create matter without universe
        # (Matter(universe=Universe())) # create matter with universe
    ]
)
def test_create_matter_without_law(matter):
    assert matter.props == {}
    assert matter.laws == {}
    assert matter.universe == None
    assert isinstance(matter.system, System)

@pytest.mark.xfail
def test_create_matter_that_already_have_law(matter_with_lawlist):
    assert len(matter_with_lawlist.props) == 3
    assert len(matter_with_lawlist.laws) == 1

@pytest.mark.xfail
# @pytest.mark.parametrize('matter', [earth, star])
def test_create_customize_macro_matter(matter):

    # not implemented
    assert matter.get_law('newton_first_law') == NewtonFirstLaw
    assert len(matter.laws) == 1
    assert matter.get_prop('mass') == prop.Mass
    assert len(matter.props) == 3

################################################################
### TEST ADD LAW AND PROPERTY TO MATTER


def test_add_law_to_matter(matter_without_law):
    matter_without_law.add_law(NewtonFirstLaw)

    assert len(matter_without_law.laws) == 1
    assert len(matter_without_law.props) == 3

@pytest.mark.xfail
def test_remove_law_from_matter(star):
    # not implemented
    star.remove_law(NewtonFirstLaw)
    assert len(star.laws) == 0
    assert len(star.props) == 0

def test_add_prop_class_to_matter(matter_without_law):
    matter_without_law.add_prop(prop.Mass)

    assert len(matter_without_law.laws) == 0
    assert len(matter_without_law.props) == 1

def test_add_prop_instance_to_matter(matter_without_law, mass):
    matter_without_law.add_prop(mass)

    assert len(matter_without_law.laws) == 0
    assert len(matter_without_law.props) == 1


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

##################################################################

def test_add_get_property_of_matter_from_system(matter_with_lawlist):
    matter_with_lawlist.set_prop('mass', 28 * Unit.KILOGRAM, t=3)

    assert matter_with_lawlist.get_prop('mass', t=3) == 28 * Unit.KILOGRAM

    matter_with_lawlist.set_prop('mass', None, t=3)
    assert matter_with_lawlist.get_prop('mass', t=3) == None
    assert matter_with_lawlist.get_prop('mass', t=9) == None
