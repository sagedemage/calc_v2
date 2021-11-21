"""Testing Subtraction"""

import pandas as pd
from calc.calculations.subtraction import Subtraction


def test_subtraction():
    """Testing subtraction method"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/subtraction/subtraction.csv")
    # Read in columns of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        subtraction = Subtraction(value1[i], (value2[i],))
        # Act and Assert
        assert subtraction.get_result() == result[i]


def test_subtraction_three_values():
    """Testing subtraction method for three values"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/subtraction/subtraction_3_values.csv")
    # Read in columns of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    value3 = dataframe["value_3"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        subtraction = Subtraction(value1[i], (value2[i], value3[i]))
        # ACt and Assert
        assert subtraction.get_result() == result[i]
