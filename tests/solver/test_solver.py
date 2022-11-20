import pytest

# from lexios.solver.solver import Solver
from lexios.unit import Unit


def test_solver(fully_customized_matter):
    fully_customized_matter.set_prop("mass", 10 * Unit.KILOGRAM, t=1)
