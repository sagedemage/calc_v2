"""Testing Addition"""

from calc.calculations.division import Division


def test_division():
    """Testing division method"""
    division1 = Division(4, 2)
    assert division1.get_result() == 2


def test_division_by_zero():
    """Testing division by zero"""
    division = Division(2, 0)
    assert division.get_result() == 0
