"""Testing Subtraction"""

from calc.calculations.subtraction import Subtraction


def test_subtraction():
    """Testing subtraction method"""
    # Arrange
    subtraction = Subtraction(2, (1,))
    # Act and Assert
    assert subtraction.get_result() == 1
