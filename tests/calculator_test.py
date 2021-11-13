"""Import the calculator class"""
import pytest

from calc.calculator import Calculator


@pytest.fixture
def fixture_clear_history():
    """Function runs each time a test method runs"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()


def test_calculator_add(fixture_clear_history):
    """Testing addition method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Adding two numbers
    assert Calculator.add_number(2, (3,)) == 5
    # Adding more than two numbers
    assert Calculator.add_number(2, (2, 2)) == 6


def test_calculator_subtract(fixture_clear_history):
    """Testing subtract method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Subtracting two numbers
    assert Calculator.subtract_number(10, (5,)) == 5

    # Subtracting more than two numbers
    assert Calculator.subtract_number(10, (2, 2)) == 6


def test_calculator_multiply(fixture_clear_history):
    """Testing the multiplication method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Multiplying two numbers
    assert Calculator.multiply_number(3, (2,)) == 6

    # Multiplying more than two numbers
    assert Calculator.multiply_number(2, (2, 2)) == 8


def test_calculator_divide(fixture_clear_history):
    """Testing division method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Dividing two numbers
    assert Calculator.divide_number(4, (2,)) == 2

    # Dividing more than two numbers
    assert Calculator.divide_number(8, (2, 2)) == 2


def test_calculator_divide_by_zero(fixture_clear_history):
    """Testing division by zero"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Dividing two numbers
    assert Calculator.divide_number(2, (0,)) is None

    # Dividing more than two numbers
    assert Calculator.divide_number(5, (0, 0)) is None


def test_calculator_history_static_property(fixture_clear_history):
    """Testing number of calculations in history"""
    # pylint: disable=unused-argument, redefined-outer-name
    Calculator.add_number(2, (2,))
    Calculator.subtract_number(3, (1,))
    Calculator.multiply_number(4, (5,))
    Calculator.divide_number(10, (2,))
    assert Calculator.count_history() == 4


def test_calculator_get_first_element_in_history(fixture_clear_history):
    """Testing getting the first result from history"""
    # pylint: disable=unused-argument, redefined-outer-name
    Calculator.add_number(2, (2,))
    Calculator.subtract_number(3, (1,))
    Calculator.multiply_number(4, (5,))
    Calculator.divide_number(10, (2,))
    assert Calculator.get_result_of_first_calculation_in_history() == 4


def test_calculator_get_last_element_in_history(fixture_clear_history):
    """Testing getting the last result from history"""
    # pylint: disable=unused-argument, redefined-outer-name
    Calculator.add_number(2, (2,))
    Calculator.subtract_number(3, (1,))
    Calculator.multiply_number(4, (5,))
    Calculator.divide_number(10, (2,))
    assert Calculator.get_result_of_last_calculation_in_history() == 5


def test_calculator_delete_history(fixture_clear_history):
    """Testing deleting an item in history"""
    # pylint: disable=unused-argument, redefined-outer-name
    Calculator.add_number(2, (2,))
    Calculator.subtract_number(3, (1,))
    Calculator.multiply_number(4, (5,))
    Calculator.divide_number(10, (2,))
    Calculator.delete_history(0)
    assert Calculator.history[0].get_result() == 2


def test_calculator_clear_history(fixture_clear_history):
    """Testing clearing the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    Calculator.add_number(2, (2,))
    Calculator.subtract_number(3, (1,))
    Calculator.multiply_number(4, (5,))
    Calculator.divide_number(10, (2,))
    Calculator.clear_history()
    assert Calculator.history == []
