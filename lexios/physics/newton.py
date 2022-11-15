from __future__ import annotations

import lexios.core.property as prop
from lexios.core.law import Law
from lexios.core.property import Acceleration, Force, Mass


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

# class VelocityDistanceTime(Law):
#     """v = s/t"""
#     def __init__(self):
#         self.props = prop.PropList()
