""" This is the Calculations class """
from calculator.calculator import Calculator
UTIME = 0
VAL1 = 1
VAL2 = 2
OPERATION = 3
RESULT = 4

class Calculations:
    """ This is the Calculations class"""

    # calc history will save calculation objects
    calc_history = []

    # @staticmethod
    # def add_calculation_to_history(calculation):
    #     """ Adds a calculation object to the history list"""
    #     Calculations.calc_history.append(calculation)
    #     return True

    @staticmethod
    def add_calculation_to_history(utime, val1, val2, operation):
        """ Adds a calculation object to the history list"""
        Calculations.calc_history.append([utime, val1, val2, operation])
        return True

    @staticmethod
    def get_last_result_in_history():
        """ Returns the last calculation (-1 signifies the last value in the list) """
        return Calculations.calc_history[-1].get_result()

    @staticmethod
    def get_first_result_in_history():
        """ Returns the last calculation (0 is the first value in the list) """
        return Calculations.calc_history[0].get_result()

    @staticmethod
    def count_history():
        """ Returns the number of calculations """

    # @staticmethod
    # def get_calc_result_history():
    #     """ This returns a list of calculation results from oldest to newest """
    #     result_list = []
    #     for item in Calculations.calc_history:
    #         result_list.append(item.get_result())
    #         # print (result_list[-1])
    #     return result_list

    @staticmethod
    def get_calc_result_history():
        """ This returns a list of calculation results from oldest to newest """
        global VAL1, VAL2, OPERATION
        temp_list = []
        for row in Calculations.calc_history:
            temp_row = row
            result = getattr(Calculator, row[OPERATION])([row[VAL1], row[VAL2]])
            temp_row.append(result)
            temp_list.append(temp_row)
        return temp_list

    @staticmethod
    def clear_calc_history():
        """ This clears the calc_history list """
        Calculations.calc_history.clear()
        return True
