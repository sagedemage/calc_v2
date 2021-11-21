"""Testing Addition"""

import pandas as pd
from calc.calculations.multiplication import Multiplication


def test_multiplication():
    """Testing multiplication method"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/multiplication/multiplication.csv")
    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        multiplication = Multiplication(value1[i], (value2[i],))
        # Act and Assert
        assert multiplication.get_result() == result[i]


def test_multiplication_three_values():
    """Testing multiplication method for three values"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/multiplication/multiplication_3_values.csv")
    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    value3 = dataframe["value_3"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        multiplication = Multiplication(value1[i], (value2[i], value3[i]))
        # Act and Assert
        assert multiplication.get_result() == result[i]
