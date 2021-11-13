""" This is the division calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """The Division class """
    # It has one method to get the result of the the calculation A and B come from
    # the calculation parent class"""

    def get_result(self):
        """Divide numbers"""
        result = self.value_a
        try:
            for value in self.values:
                result = result / value
        except ZeroDivisionError:
            result = None
        return result
