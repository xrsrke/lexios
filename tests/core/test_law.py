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
def nonempty_law_list():
    laws = [NewtonFirstLaw]
    return law.LawList(laws)

@pytest.fixture
def empty_law_list():
    laws = []
    return law.LawList(laws)

# @pytest.mark.parametrize(
#     'law_list, expected_n_laws',
#     [
#         (lazy_fixture('nonempty_law_list'), 1),
#         (lazy_fixture('empty_law_list'), 0)
#     ]
# )
def test_create_empty_law_list(empty_law_list):
    assert len(empty_law_list.laws) == 0

def test_create_nonempty_law_list(nonempty_law_list):
    assert len(nonempty_law_list.laws) == 1
    assert issubclass(nonempty_law_list.laws['newton_first_law'], NewtonFirstLaw)

# def test_add_an_law_to_lawlist(law_list):
#     pass

# def test_remove_an_law_from_lawlist(law_list):
#     pass
