"""Import the calculator class"""

from calc.calculator import Calculator


def test_calculator():
    """Testing Calculator's default result is empty"""
    calc1 = Calculator()
    assert calc1.history == []


def test_calculator_add():
    """Testing addition method"""
    calc1 = Calculator()
    assert calc1.add_number(2, 2) == 4


def test_calculator_subtract():
    """Testing subtract method"""
    assert Calculator.subtract_number(2, 1) == 1


def test_calculator_multiply():
    """Testing the multiplication method"""
    assert Calculator.multiply_number(1, 2) == 2


def test_calculator_divide():
    """Testing division method"""
    assert Calculator.divide_number(2, 2) == 1


def test_calculator_divide_by_zero():
    """Testing division by zero"""
    assert Calculator.divide_number(2, 0) == 0


def test_calculator_history_static_property():
    """Testing number of calculations in history"""
    calc1 = Calculator()
    calc1.add_number(1, 2)
    assert calc1.count_history() == 6


def test_calculator_history_get_addition_calculation():
    """Testing getting the result from history"""
    calculation = Calculator.history[0]
    assert calculation.get_result() == 4


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
