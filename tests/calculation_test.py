"""Import calculation class"""

from calc.calculations.calculation import Calculation


def test_get_calculation_values():
    """Get Calculation values"""
    calculation = Calculation(1, 2)
    assert calculation.get_value_a() == 1
    assert calculation.get_value_b() == 2
