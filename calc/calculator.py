""" content of calculator.py """
from calc.calculations.subtraction import Subtraction
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class Calculator:
    """Calculator class"""
    history = []

    @staticmethod
    def add_number(value_a, value_b):
        """adds two numbers"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_number(value_a, value_b):
        """Subtract a Number"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(value_a, value_b):
        """Multiply a Number"""
        multiplication = Multiplication(value_a, value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_number(value_a, value_b):
        """Divide a Number"""
        division = Division(value_a, value_b)
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

    @staticmethod
    def delete_history(index):
        """Delete item from history"""
        Calculator.history.pop(index)
