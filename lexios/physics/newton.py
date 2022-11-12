from lexios.core.law import Law
from lexios.core.property import Force, Mass, Acceleration

class NewtonFirstLaw(Law):
    """Newton First Law of Motion"""
    def __init__(self):
        super().__init__()
        self.props = [
            {'prop': Force},
            {'prop': Mass},
            {'prop': Acceleration}
        ]
    
    def expr(self): pass