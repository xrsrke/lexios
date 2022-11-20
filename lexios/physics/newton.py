"""Implementation of newton's laws."""
from __future__ import annotations

import lexios.core.property as prop
from lexios.core.law import Law


class NewtonFirstLaw(Law):
    """Newton First Law of Motion."""

    def __init__(self):
        """Initialize the law."""
        super().__init__()
        # self.props = [
        #     {'prop': Force},
        #     {'prop': Mass},
        #     {'prop': Acceleration}
        # ]
        self.props = prop.PropList([prop.Force, prop.Mass, prop.Acceleration])

    def expr(self):
        """Symbolic expression of the law."""
        pass


class WeightOnEarth:
    """Weight of an object on the Earth's surface."""

    def __init__(self):
        """Initialize the weight on the Earth's surface."""
        super().__init__()
        self.props = prop.PropList([prop.Mass, prop.Weight, prop.GravityAcceleration])

    def expr(self):
        """Symbolic expression of the law."""
        pass
