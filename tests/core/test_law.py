from __future__ import annotations

import pytest
from pytest_lazyfixture import lazy_fixture

import lexios.core.law as law
from lexios.matter import MacroMatter
from lexios.physics.newton import NewtonFirstLaw


@pytest.mark.parametrize(
    'law, expected_n_props',
    [
        (lazy_fixture('law_with_property'), 3),
        (lazy_fixture('law_without_property'), 0)
    ]
)
def test_create_law(law, expected_n_props):
    assert len(law.props) == expected_n_props
    assert law.matter == None

##################################
# FOR LAW LIST

@pytest.fixture
def law_list():
    laws = []
    return law.LawList(laws)

def test_create_law_list(law_list):
    assert len(law_list) == 3

def test_add_an_law_to_lawlist(law_list):
    pass

def test_remove_an_law_from_lawlist(law_list):
    pass
