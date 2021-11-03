""" content of addition.py"""
from calc.calculations.calculation import Calculation


class Addition(Calculation):
    """Addition class"""

    def get_result(self):
        """Add two numbers"""
        result = self.value_a + self.value_b
        return result
