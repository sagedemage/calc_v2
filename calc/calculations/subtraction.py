""" This is the subtraction calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """The Subtraction class """
    # It has one method to get the result of the the calculation A and B come from
    # the calculation parent class

    def get_result(self):
        """Subtract two numbers"""
        result = self.value_a
        for value in self.values:
            result = result - value
        return result
