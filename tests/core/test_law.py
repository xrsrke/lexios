from lexios.matter import MarcoMatter
from lexios.physics.newton import NewtonFirstLaw

def test_law_without_expr():
    law = NewtonFirstLaw()
    assert law.matter == None

def test_law_with_matter():
    matter = MarcoMatter()

def test_create_law():
    pass