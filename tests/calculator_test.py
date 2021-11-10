"""Import the calculator class"""

from calc.calculator import Calculator


def test_calculator():
    """Testing Calculator's default result is empty"""
    assert Calculator.history == []


def test_calculator_add():
    """Testing addition method"""
    assert Calculator.add_number(2, 3) == 5


def test_calculator_add_more_than_two_values():
    """Testing addition method with more than two values"""
    assert Calculator.add_number(2, 2, 2) == 6


def test_calculator_subtract():
    """Testing subtract method"""
    assert Calculator.subtract_number(10, 5) == 5


def test_calculator_subtract_more_than_two_values():
    """Testing subtraction method with more than two values"""
    assert Calculator.subtract_number(10, 2, 2) == 6


def test_calculator_multiply():
    """Testing the multiplication method"""
    assert Calculator.multiply_number(3, 2) == 6


def test_calculator_multiply_more_than_two_values():
    """Testing multiplication method with more than two values"""
    assert Calculator.multiply_number(2, 2, 2) == 8


def test_calculator_divide():
    """Testing division method"""
    assert Calculator.divide_number(4, 2) == 2


def test_calculator_divide_more_than_two_values():
    """Testing division method with more than two values"""
    assert Calculator.divide_number(8, 2, 2) == 2


def test_calculator_divide_by_zero():
    """Testing division by zero"""
    # The program throws ZeroDivisionError
    # Result being 0 means the result value did not change
    # It does not mean the answer is actually equal to 0
    assert Calculator.divide_number(2, 0) == 0


def test_calculator_divide_by_zero_more_than_once():
    """Testing division method with more than two values"""
    # The program throws ZeroDivisionError
    # Result being 0 means the result value did not change
    # It does not mean the answer is actually equal to 0
    assert Calculator.divide_number(5, 0, 0) == 0


def test_calculator_history_static_property():
    """Testing number of calculations in history"""
    assert Calculator.count_history() == 10


def test_calculator_get_first_element_in_history():
    """Testing getting the first result from history"""
    assert Calculator.get_result_of_first_calculation_in_history() == 5


def test_calculator_get_last_element_in_history():
    """Testing getting the last result from history"""
    assert Calculator.get_result_of_last_calculation_in_history() == 0


def test_calculator_delete_history():
    """Testing deleting an item in history"""
    # Index: 0 Value:5
    # Index: 1 Value:6
    Calculator.delete_history(0)
    assert Calculator.history[0].get_result() == 6


def test_calculator_clear_history():
    """Testing clearing the history"""
    Calculator.clear_history()
    assert Calculator.history == []
