import pytest
from lexios.matter import MarcoMatter
from lexios.physics.newton import NewtonFirstLaw
import lexios.core.law as law

def test_law_without_expr():
    law = NewtonFirstLaw()
    assert law.matter == None

def test_law_with_matter():
    law = NewtonFirstLaw()

@pytest.fixture
def law_without_property():
    pass

@pytest.fixture
def newton_first_law():
    return NewtonFirstLaw()

@pytest.mark.parametrize('law', [newton_first_law])
def test_create_law():
    assert len(law.props) == 3 

def test_create_law_without_property():
    pass

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

def test_create_property_list(prop_list):
    assert len(prop_list) == 3
    assert len(list(iter(prop_list))) == 3