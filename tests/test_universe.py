import pytest
from lexios.universe import Universe


def test_create_universe():
    universe = Universe()
    assert universe.laws == {}
    assert universe.props == {}

class OurUniverse(Universe):
    def __init__(self):
        # TODO: implement this
        self.laws = []

@pytest.fixture
def our_universe():
    return OurUniverse()