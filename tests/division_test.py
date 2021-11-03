"""Testing Addition"""

from calc.calculations.division import Division


def test_division():
    """Testing addition method"""
    division1 = Division(4, 2)
    division2 = Division(2, 0)
    assert division1.get_result() == 2
    assert division2.get_result() == 0
