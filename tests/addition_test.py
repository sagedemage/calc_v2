"""Testing Addition"""

from calc.calculations.addition import Addition


def test_addition():
    """Testing addition method"""
    # Arrange
    addition = Addition(1, (2,))
    # Act
    result = addition.get_result()
    # Assert
    assert result == 3
