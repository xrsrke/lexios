from __future__ import annotations

import pytest

from lexios.symbolic.symbol import Symbol
from lexios.unit import Unit


def test_create_system(system):
    assert system._states['x'] == 1

def test_add_matter_to_system(matter_with_lawlist, system):
    matter_with_lawlist.system = system
    assert matter_with_lawlist.system == system

def test_get_symbolic_property_of_matter_from_system(matter_with_lawlist):
    system = matter_with_lawlist.system
    assert isinstance(system.get_prop('mass', t=1, instance=matter_with_lawlist), Symbol)

def test_eval_property_of_matter_from_system(matter_with_lawlist):
    pass

def test_set_property_of_matter_from_system(matter_with_lawlist):
    system = matter_with_lawlist.system
    value = 6.9 * Unit.KILOGRAM
    system.set_prop('mass', value, t=1, instance=matter_with_lawlist)

    # assert system.get_prop('mass', value, t=1, instance=matter_with_lawlist) ==
