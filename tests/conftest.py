from __future__ import annotations

from typing import List

import pytest

import lexios.core.law as law
import lexios.core.property as prop
import lexios.matter as matter
import lexios.system
import lexios.universe
from lexios.callback.core import Callback
from lexios.physics.newton import NewtonFirstLaw
from lexios.unit import Unit, unit_convert


class LawWithoutProperty(law.Law):
    def __init__(self):
        super().__init__()

    def expr(self):
        pass


class LawWithProperty(law.Law):
    def __init__(self):
        super().__init__()
        self.props = prop.PropList([prop.Mass, prop.Mole, prop.Force])

    def expr(self):
        pass


@pytest.fixture
def law_without_property():
    return LawWithoutProperty()


@pytest.fixture
def law_with_property():
    return LawWithProperty()


class MatterWithoutLaw(matter.MacroMatter):
    def __init__(self):
        super().__init__()


class MatterWithLawList(matter.MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = law.LawList([NewtonFirstLaw])


class MatterWithLaw(matter.MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = [NewtonFirstLaw]
        for law in self.laws:
            name = law.class_name()
            self.add_law(name, law)


@pytest.fixture
def mass():
    return prop.Mass()


@pytest.fixture
def matter_without_law():
    return MatterWithoutLaw()


@pytest.fixture
def matter_with_lawlist():
    return MatterWithLawList()


@pytest.fixture
def matter_with_law():
    return MatterWithLaw()


################################################################
# SYSTEM


@pytest.fixture
def system():
    return lexios.system.System()


################################################################
# Universe


@pytest.fixture
def universe():
    return lexios.universe.Universe()


# class OurUniverse(Universe):
#     pass

# def our_universe():
#     pass


################################################################
# Callback


class ConvertToPoundCallback(Callback):
    def convert_to_pound(self, quantity):
        return unit_convert(quantity, Unit.POUND)

    def after_get_prop(self):
        pass


class RoundSignificantFigure(Callback):
    pass


class LogPracticeCallback(Callback):
    pass


class LogEverythingCallback(Callback):
    pass


@pytest.fixture
def convert_to_pound_callback():
    return ConvertToPoundCallback


@pytest.fixture
def three_cbs():
    return [ConvertToPoundCallback, LogPracticeCallback, LogEverythingCallback]


@pytest.fixture
def law_with_property_and_callback(law_with_property, convert_to_pound_callback):
    law_with_property.add_cb(convert_to_pound_callback)
    return law_with_property


class FullyCustomizedLaw(law.Law):
    def __init__(self):
        super().__init__()
        self.props = prop.PropList([prop.Mass, prop.Mole, prop.Force])
        self.add_cbs([convert_to_pound_callback])

    def expr(self):
        pass


class FullyCustomizedMatter(matter.MacroMatter):
    def __init__(self):
        super().__init__()
        self.laws = law.LawList([FullyCustomizedLaw])


@pytest.fixture
def fully_customized_matter():
    return FullyCustomizedMatter()
