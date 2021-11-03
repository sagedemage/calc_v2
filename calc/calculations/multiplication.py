""" content of multiplication.py """
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """Multiplication class"""

    def get_result(self):
        """Multiply two numbers"""
        result = self.value_a * self.value_b
        return result
