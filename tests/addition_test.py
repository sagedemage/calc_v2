"""Testing Addition"""

from calc.calculations.addition import Addition


def test_addition():
    """Testing addition method"""
    # Arrange
    addition = Addition(1, 2)
    # Act and Assert
    assert addition.get_result() == 3
