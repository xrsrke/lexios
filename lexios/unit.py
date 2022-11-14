from enum import Enum
from dataclasses import dataclass

import sympy.physics.units as u


@dataclass(frozen=True)
class Unit:
    """
    Default SI Units
    """
    LENGTH = u.meter
    MASS = u.kilogram
    TIME = u.second
    TEMPERATURE = u.kelvin

    """
    For chemistry
    """
    MOLAR_MASS = u.gram / u.mole
    MOLE = u.mole
    SPECIFIC_HEAT = u.joule / (u.kilogram * u.kelvin)
    PRESSURE = u.pascal
    VOLUME = u.liter
    
    """For Physics"""
    FORCE = u.force
    ACCELERATION = u.acceleration
    VELOCITY = u.velocity
    
    KILOGRAM = u.kilogram
    GRAM = u.gram

def str2unit(value: str):
    pass

def convert_to(expr, target_units: Unit):
    return u.convert_to(expr, target_units)

def round():
    pass