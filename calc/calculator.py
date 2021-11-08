""" content of calculator.py """
from calc.calculations.subtraction import Subtraction
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculator:
    """Calculator class"""
    history = []

    @staticmethod
    def add_number(value1, *values):
        """Add numbers by infinite amount of times"""
        result = value1
        for val in values:
            addition = Addition.create(result, val)
            result = addition.get_result()
        Calculator.add_history(addition)
        return addition.get_result()

    @staticmethod
    def subtract_number(value1, *values):
        """Subtract numbers by infinite amount of times"""
        result = value1
        for val in values:
            subtraction = Subtraction.create(result, val)
            result = subtraction.get_result()
        Calculator.add_history(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(value1, *values):
        """Multiply numbers by infinite amount of times"""
        result = value1
        for val in values:
            multiplication = Multiplication.create(result, val)
            result = multiplication.get_result()
        Calculator.add_history(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_number(value1, *values):
        """Divide numbers by infinite amount of times"""
        result = value1
        for val in values:
            division = Division.create(result, val)
            result = division.get_result()
        Calculator.add_history(division)
        return division.get_result()

    @staticmethod
    def count_history():
        """Counting the number of items in history"""
        count = len(Calculator.history)
        return count

    @staticmethod
    def clear_history():
        """Clear history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def delete_history(index):
        """Delete item from history"""
        Calculator.history.pop(index)
        return True

    @staticmethod
    def add_history(class_object):
        """Add object to history"""
        Calculator.history.append(class_object)
        return True

    @staticmethod
    def get_result_of_first_calculation_in_history():
        """Get first result from history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_result_of_last_calculation_in_history():
        """Get last result from history"""
        return Calculator.history[-1].get_result()
