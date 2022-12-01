"""Implementation of Unit class."""

from dataclasses import dataclass

import sympy.physics.units as u


@dataclass(frozen=True)
class Unit:
    """Default SI Units."""

    LENGTH = u.meter
    MASS = u.kilogram
    TIME = u.second
    TEMPERATURE = u.kelvin

    """For chemistry."""
    MOLAR_MASS = u.gram / u.mole
    MOLE = u.mole
    SPECIFIC_HEAT = u.joule / (u.kilogram * u.kelvin)
    PRESSURE = u.pascal
    VOLUME = u.liter

    """For Physics."""
    FORCE = u.force
    ACCELERATION = u.acceleration
    VELOCITY = u.velocity

    KILOGRAM = u.kilogram
    GRAM = u.gram
    POUND = u.pound
    NEWTON = u.newton
    METER = u.meter
    SECOND = u.second


def str2unit(value: str):
    """A function convert a string to unit."""
    pass


def unit_convert(quantity, target_units: Unit):
    """A function convert between units."""
    return u.convert_to(quantity, target_units)


def round():
    """A function round a number to significant figures."""
    pass
