""" content of division.py """
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """Division class"""

    def get_result(self):
        """Divide two numbers"""
        result = 0
        try:
            result = self.value_a / self.value_b
        except ZeroDivisionError as message:
            mes = message
            print(mes)
        return result
