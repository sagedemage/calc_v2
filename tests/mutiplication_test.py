"""Testing Addition"""

from calc.calculations.multiplication import Multiplication


def test_multiplication():
    """Testing multiplication method"""
    multiplication = Multiplication(1, 2)
    assert multiplication.get_result() == 2
