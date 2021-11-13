""" This is the addition calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


# This is how you extend the Addition class with Calculation
class Addition(Calculation):
    """The Addition class """
    # It has one method to get the result of the the calculation A and B come from
    # the calculation parent class

    def get_result(self):
        """Add numbers"""
        result = self.value_a
        for value in self.values:
            result = result + value
        return result
