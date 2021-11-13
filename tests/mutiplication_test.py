"""Testing Addition"""

from calc.calculations.multiplication import Multiplication


def test_multiplication():
    """Testing multiplication method"""
    # Arrange
    multiplication = Multiplication(1, (2,))
    # Act and Assert
    assert multiplication.get_result() == 2
