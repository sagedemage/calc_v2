"""This is our calculation base class / Abstract Class"""


class Calculation:
    """ Calculation Class """
    # Default Constructor
    def __init__(self, value_a, values: tuple):
        """Initialize the values"""
        self.value_a = value_a
        self.values = Calculation.number_list(values)

    @staticmethod
    def number_list(values):
        """Put numbers in list"""
        list_number = []
        for value in values:
            list_number.append(value)
        return tuple(list_number)

    # Class Factory Method <- bound to the class and
    # not the instance of the class
    @classmethod
    def create(cls, value_a, values: tuple):
        """Factory Method"""
        return cls(value_a, values)
