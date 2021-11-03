""" content of subtraction.py  """
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """Subtraction class"""

    def get_result(self):
        """Subtract two numbers"""
        result = self.value_a - self.value_b
        return result
