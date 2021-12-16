""" This is Calculator.py """

# These import the namespaces
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add(values):
        """ adds 2 numbers and save them to calc_history list """
        # This passes value_a and value_b to the Addition constructor which instantiates an object
        add = Addition(values)
        # This uses the base class method to get the result from the object
        return add.get_result()

    @staticmethod
    def subtract(values):
        """ adds 2 numbers and save them to calc_history list """
        # This instantiates a Subtraction object which passes value_a and value_b to the constructor
        sub = Subtraction(values)
        # This uses the base class method to get the result from the object
        return sub.get_result()

    @staticmethod
    def multiply(values):
        """ adds 2 numbers and save them to calc_history list """
        # This instantiates a Multiplication object which passes value_a and value_b
        # to the constructor
        mult = Multiplication(values)
        # This uses the base class method to get the result from the object
        return mult.get_result()

    @staticmethod
    def divide(values):
        """ divides the first value by the list of values and save them to calc_history list """
        # This instantiates a Division object which passes value_a and value_b to the constructor
        div = Division(values)
        # This uses the base class method to get the result from the object
        return div.get_result()
