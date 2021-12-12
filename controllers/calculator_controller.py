from history.calculations import Calculations
from calculator.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for, session
from csv_util.file_utils import Filehandler

class CalculatorController:
    @staticmethod
    def post():
        """ Get data and post values to form """
        if request.form['value1'] != '' and request.form['value2'] != '':
            # get the values out of the form
            value1 = float(request.form['value1'])
            value2 = float(request.form['value2'])
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            result = getattr(Calculator, operation)(my_tuple)  # use combined function todo
            Calculations.add_calculation_to_history(value1, value2, operation)

            return render_template('result.html', data=Calculations.get_calc_result_history(),
                                   value1=value1, value2=value2, operation=operation, result=result)

        flash("You must enter a value for BOTH value 1 and value 2")
        error = 'You must enter a value for value 1 and or value 2'
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """ Get Blank form """
        return render_template('calculator.html')








