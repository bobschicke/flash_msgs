""" These are the tests for the Calculator """

from calculator.calculator import Calculator

def test_calculator_add():
    """ Tests Addition of 2 numbers"""
    assert Calculator.add((5, 4, 2)) == 11

def test_calculator_add_nan():
    """ Tests Addition of numbers with a string as one of the values"""
    assert Calculator.add((5, 'x', 2)) == "nan"


def test_calculator_subtract():
    """ Tests Subtraction of 2 numbers """
    assert Calculator.subtract((10, 4, 2)) == 4

def test_calculator_subtract_nan():
    """ Tests Addition of numbers with a string as one of the values"""
    assert Calculator.subtract((5, 'x', 2)) == "nan"


def test_calculator_multiply():
    """ Tests Multiplication of two numbers """
    assert Calculator.multiply((5, 4, 2)) == 40

def test_calculator_multiply_nan():
    """ Tests Addition of numbers with a string as one of the values"""
    assert Calculator.multiply((5, 'x', 2)) == "nan"

def test_calculator_divide():
    """ Tests Division of two numbers """
    assert Calculator.divide((120, 10, 4)) == 3

def test_calculator_divide_by0():
    """ Tests that Division by Zero catches the error and doesn't crash the program """
    assert Calculator.divide((10, 5, 0)) == "DivBy0"

def test_calculator_divide_nan():
    """ Tests Addition of numbers with a string as one of the values"""
    assert Calculator.divide((5, 'x', 2)) == "nan"
