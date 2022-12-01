from __future__ import annotations

import pytest
from pytest_lazyfixture import lazy_fixture

import lexios.core.law as law
from lexios.callback.core import Callback
from lexios.physics.newton import NewtonFirstLaw
from lexios.unit import Unit


@pytest.mark.parametrize(
    "law, expected_n_props", [(lazy_fixture("law_with_property"), 3), (lazy_fixture("law_without_property"), 0)]
)
def test_create_law(law, expected_n_props):
    assert len(law.props) == expected_n_props
    assert law.matter is None


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
    assert issubclass(nonempty_law_list.laws["newton_first_law"], NewtonFirstLaw)


# def test_add_an_law_to_lawlist(law_list):
#     pass

# def test_remove_an_law_from_lawlist(law_list):
#     pass


########################################################################
# Callback


@pytest.mark.parametrize("law", [(lazy_fixture("law_with_property"))])
def test_add_callbacks_to_law(law, three_cbs):
    law.add_cbs(three_cbs)

    assert len(law.cbs) == 3
    assert isinstance(law.cbs[0], Callback)

    first_cb = law.cbs[0]
    assert first_cb.law == law
    assert first_cb.props == law.props
    assert first_cb.matter == law.matter
    # assert first_cb.system == law.system


@pytest.mark.skip("not implemented")
def test_convert_to_pound_callbacks(fully_customized_matter):
    # TODO: implement
    MASS_IN_KG = 10 * Unit.KILOGRAM
    MASS_IN_POUND = 22.046 * Unit.POUND

    fully_customized_matter.add_prop("mass", MASS_IN_KG, t=1)

    assert fully_customized_matter.get_prop("mass", t=1).eval() == MASS_IN_POUND


@pytest.mark.parametrize("cb", [lazy_fixture("convert_to_pound_callback")])
def test_remove_a_callback_from_law(law_with_property_and_callback, cb):
    # TODO: cbs in property is instance, cb in test is class => can't find
    law_with_property_and_callback.remove_cb(cb)

    assert len(law_with_property_and_callback.cbs) == 0
