from __future__ import annotations

import pytest

from lexios.universe import Universe


def test_create_universe(universe):
    assert universe.laws == {}
    assert universe.props == {}

# @pytest.fixture
# def our_universe():
#     return OurUniverse()
