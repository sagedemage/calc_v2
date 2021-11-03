"""This is our calculation base class / Abstract Class"""


class Calculation:
    """ Default Constructor """
    def __init__(self, value_a, value_b):
        """Initialize the values"""
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method <- bound to the class and
    # not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        """Class method to create the Class"""
        return cls(value_a, value_b)

    def get_value_a(self):
        """Get value of the first value"""
        return self.value_a

    def get_value_b(self):
        """Get value of the second value"""
        return self.value_b
