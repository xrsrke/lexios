"""Some useful callbacks."""

from lexios.callback.core import Callback
from lexios.unit import Unit, unit_convert


class SignificantFigureCallback(Callback):
    """Round significant figures callback."""

    order = 10

    def round_significant_figure(self):
        """Round significant figures."""
        pass

    def after_change_prop(self):
        """After change property."""
        pass


class ConvertToPoundCallback(Callback):
    """Convert all mass property to pound callback."""

    order = 5
    PROP_NAME = "mass"

    def convert_to_pound(self, quantity):
        """Convert quantity to pound callback."""
        return unit_convert(quantity, Unit.POUND)

    def before_change_prop(self):
        """Before change property."""
        if self.prop("name") == self.PROP_NAME:
            self.prop = self.convert_to_pound(self.prop("value"))


class ConservationOfMassCallback(Callback):
    """Conservation of mass callback."""

    def __init__(self):
        """Initialize the conservation of mass callback."""
        self.mass_in_env = 0

    def calculate_mass_env(self):
        """Calculate mass environment."""
        last_mass = self.prop("value", t=-1)
        current_mass = self.prop("value", t=0)

    def after_change_prop(self):
        """After change property."""
        if self.prop("dim") == "mass":
            self.calculate_mass_env()
