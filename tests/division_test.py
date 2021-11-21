"""Testing Addition"""

import pandas as pd
from calc.calculations.division import Division


def test_division():
    """Testing division method"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/division/division.csv")
    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        division = Division(value1[i], (value2[i],))
        # Act and Assert
        assert division.get_result() == result[i]


def test_division_three_values():
    """Testing multiplication method for three values"""
    # Read in the csv file
    dataframe = pd.read_csv("tests/test_data/division/division_3_values.csv")
    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    value3 = dataframe["value_3"]
    result = dataframe["result"]

    for i in range(result.size):
        # Arrange
        division = Division(value1[i], (value2[i], value3[i]))
        # Act and Assert
        assert division.get_result() == result[i]


def test_division_by_zero():
    """Testing division by zero"""
    # Arrange
    division1 = Division(5, (0,))
    division2 = Division(5, (0, 0))
    # Act and Assert
    assert division1.get_result() is None
    assert division2.get_result() is None
