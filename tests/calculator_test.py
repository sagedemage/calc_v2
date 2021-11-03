"""Import the calculator class"""

from calc.calculator import Calculator


def test_calculator():
    """Testing Calculator's default result is empty"""
    calc1 = Calculator()
    assert calc1.history == []


def test_calculator_add():
    """Testing addition method"""
    calc1 = Calculator()
    assert calc1.add_number(2, 2, 2) == 6


def test_calculator_subtract():
    """Testing subtract method"""
    assert Calculator.subtract_number(10, 2, 2) == 6


def test_calculator_multiply():
    """Testing the multiplication method"""
    assert Calculator.multiply_number(2, 2, 2) == 8


def test_calculator_divide():
    """Testing division method"""
    assert Calculator.divide_number(8, 2, 2) == 2


def test_calculator_divide_by_zero():
    """Testing division by zero"""
    assert Calculator.divide_number(2, 0) == 0


def test_calculator_history_static_property():
    """Testing number of calculations in history"""
    calc1 = Calculator()
    calc1.add_number(1, 2)
    assert calc1.count_history() == 6


def test_calculator_get_first_element_in_history():
    """Testing getting the first result from history"""
    calculation = Calculator.get_result_of_first_calculation_added_to_history()
    assert calculation == 6


def test_calculator_get_last_element_in_history():
    """Testing getting the last result from history"""
    calculation = Calculator.get_result_of_last_calculation_added_to_history()
    assert calculation == 3


def test_calculator_clear_history():
    """Testing clearing the history"""
    calc1 = Calculator()
    calc1.clear_history()
    assert calc1.history == []


def test_calculator_delete_history():
    """Testing deleting an item in history"""
    calc1 = Calculator()
    # I: 0 V:2
    calc1.add_number(1, 1)
    # I: 1 V:4
    calc1.subtract_number(6, 2)

    calc1.delete_history(0)
    assert calc1.history[0].get_result() == 4
