""" contents of calculations.py """

import pandas as pd


class Calculations:
    """Calculator class"""
    history = []
    d = {'value1': [], 'value2': [], 'result': []}

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
    def add_history(class_object):
        """Add an object to the history"""
        Calculations.history.append(class_object)
        value1 = class_object.get_value1()
        values = class_object.get_values()
        result = class_object.get_result()
        Calculations.d['value1'].append(value1)
        for value in values:
            Calculations.d['value2'].append(value)
        Calculations.d['result'].append(result)
        return True

    @staticmethod
    def write_in_csv_file():
        Calculations.df = pd.DataFrame(Calculations.d)
        Calculations.df.to_csv("output.csv", index=False)
        return True

    @staticmethod
    def get_first_calculation():
        """Get the first result from the history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_last_calculation():
        """Get the last result from the history"""
        return Calculations.history[-1].get_result()
