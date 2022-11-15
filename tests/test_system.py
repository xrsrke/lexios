from __future__ import annotations

import pytest


def test_create_system(system):
    pass

def test_add_matter_to_system(matter_with_lawlist, system):
    matter_with_lawlist.system = system
    assert matter_with_lawlist.system == system
