""" content of calculator.py """
from calc.calculations.subtraction import Subtraction
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculator:
    """Calculator class"""
    history = []

    @staticmethod
    def add_number(value, values: tuple):
        """Add as many times to the first number"""
        addition = Addition.create(value, values)
        Calculator.add_history(addition)
        return addition.get_result()

    @staticmethod
    def subtract_number(value, values: tuple):
        """Subtract as many times to the first number"""
        subtraction = Subtraction.create(value, values)
        Calculator.add_history(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(value, values: tuple):
        """Multiply as many times to the first number"""
        multiplication = Multiplication.create(value, values)
        Calculator.add_history(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_number(value, values: tuple):
        """Divide as many times to the first number"""
        division = Division.create(value, values)
        Calculator.add_history(division)
        return division.get_result()

    @staticmethod
    def count_history():
        """Counting the number of items in the history"""
        count = len(Calculator.history)
        return count

    @staticmethod
    def clear_history():
        """Clear the history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def delete_history(index):
        """Delete an item from the history"""
        Calculator.history.pop(index)
        return True

    @staticmethod
    def add_history(class_object):
        """Add an object to the history"""
        Calculator.history.append(class_object)
        return True

    @staticmethod
    def get_result_of_first_calculation_in_history():
        """Get the first result from the history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_result_of_last_calculation_in_history():
        """Get the last result from the history"""
        return Calculator.history[-1].get_result()
