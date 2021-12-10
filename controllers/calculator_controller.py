from history.calculations import Calculations
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session


class CalculatorController:
    @staticmethod
    def post():
        """ Get data and post values to form """
        if request.form['value1'] != '' and request.form['value2'] != '':
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple) # use combined function todo
            result = str(Calculator.get_last_result_value())
            # Hey if you copy this it will not work you need to think about it
            data = {
                'value1': [value1],
                'value2': [value2],
                'operation': [operation]
            }
            Calculator.writeHistoryToCSV()
            return render_template('result.html', data=Calculations.get_calc_result_history(), value1=value1, value2=value2, operation=operation, result=result)

        error = 'You must enter a value for value 1 and or value 2'
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """ Get Blank form """
        return render_template('calculator.html')


    """
    The easy calculator solution
    1.  fix your calculator to read and write calculations to the csv
    2.  fix the controller to read the the csv to history first
    3.  Fix the controller to write the history to csv after you add the calculation to history
    4.  Make a method on the calculator to return the history in the format you want to print in the template
    
    Optional
       Fix it so that you store the type of calculation and perform the calulation at runtime, 
       so you don't store the raw result
       
       IF you want to be fancy you can change the delimeter for the file to semicolon and write your tuple of value to the file
       
       Values, Operation
       1,2,3,4; Addition
       1,2,3,4; Addition
    
    """






