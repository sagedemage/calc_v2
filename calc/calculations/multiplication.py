""" This is the multiplication calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """The Multiplication class """
    # It has one method to get the result of the the calculation A and B come from
    # the calculation parent class

    def get_result(self):
        """Multiply numbers"""
        result = self.value_a
        for value in self.values:
            result = result * value
        return result
