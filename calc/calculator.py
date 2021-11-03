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
        """Add numbers"""
        value = value1
        for val in values:
            addition = Addition(value, val)
            value = addition.get_result()
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_number(value1, *values):
        """Subtract numbers"""
        value = value1
        for val in values:
            subtraction = Subtraction(value, val)
            value = subtraction.get_result()
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(value1, *values):
        """Multiply numbers"""
        value = value1
        for val in values:
            multiplication = Multiplication(value, val)
            value = multiplication.get_result()
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_number(value1, *values):
        """Divide numbers"""
        value = value1
        for val in values:
            division = Division(value, val)
            value = division.get_result()
        Calculator.history.append(division)
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

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Get first result from history"""
        result = Calculator.history[0].get_result()
        return result

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Get last result from history"""
        result = Calculator.history[-1].get_result()
        return result
