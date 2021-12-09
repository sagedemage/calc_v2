""" contents of calculations.py """

import pandas as pd


class Calculations:
    """Calculator class"""
    history = []
    d = {"operations": [], "value1": [], "value2": [], "result": []}

    @staticmethod
    def count_history():
        """Counting the number of items in the history"""
        count = len(Calculations.history)
        return count

    @staticmethod
    def clear_history():
        """Clear the history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def delete_history(index):
        """Delete an item from the history"""
        Calculations.history.pop(index)
        return True

    @staticmethod
    def put_history_to_csv(operation, value1, value2, result):
        """Write the history to csv file"""
        Calculations.d["operations"].append(operation)
        Calculations.d["value1"].append(value1)
        Calculations.d["value2"].append(value2)
        Calculations.d["result"].append(result)
        Calculations.df = pd.DataFrame(Calculations.d)
        Calculations.df.to_csv("output.csv", index=False)
        return True

    @staticmethod
    def read_csv_file():
        """Read the history from csv and put it into the history """
        df = pd.read_csv('output.csv')
        operations = df["operations"]
        value1 = df["value1"]
        value2 = df["value2"]
        result = df["result"]
        Calculations.clear_history()
        for i in range(len(result)):
            item = [operations[i], value1[i], value2[i], result[i]]
            Calculations.history.append(item)
        return True

    @staticmethod
    def get_history():
        return Calculations.history

    @staticmethod
    def add_history(class_object):
        """Add an object to the history"""
        Calculations.history.append(class_object)
        return True

    @staticmethod
    def get_first_calculation():
        """Get the first result from the history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_last_calculation():
        """Get the last result from the history"""
        return Calculations.history[-1].get_result()
