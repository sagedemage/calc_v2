"""Testing Subtraction"""

from calc.calculations.subtraction import Subtraction


def test_subtraction():
    """Testing subtraction method"""
    subtraction = Subtraction(2, 1)
    assert subtraction.get_result() == 1
