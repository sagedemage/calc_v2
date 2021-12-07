""" contents of calculations.py """


class Calculations:
    """Calculator class"""
    history = []

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
        return True

    @staticmethod
    def get_first_calculation():
        """Get the first result from the history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_last_calculation():
        """Get the last result from the history"""
        return Calculations.history[-1].get_result()
