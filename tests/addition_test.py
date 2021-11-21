"""Testing Addition"""

import pandas as pd
from calc.calculations.addition import Addition


def test_addition():
    """Testing addition method for two values"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/addition/addition.csv")
    # Read each columns of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        addition = Addition(value1[i], (value2[i],))
        # Act and Assert
        assert addition.get_result() == result[i]


def test_addition_three_values():
    """Testing addition method for three values"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/addition/addition_3_values.csv")
    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    value3 = dataframe["value_3"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        addition = Addition(value1[i], (value2[i], value3[i]))
        # ACt and Assert
        assert addition.get_result() == result[i]
