"""This is the Calculator controller"""
import time
from flask import render_template, request, flash
from history.calculations import Calculations
from calculator.calculator import Calculator
from csv_util.file_utils import Filehandler


class CalculatorController:
    """This is the Calculations Controller Class"""
    @staticmethod
    def post():
        """ Get data and post values to form """
        if request.form['value1'] != '' and request.form['value2'] != '':
            # get the values out of the form
            # to-do test for nan
            value1 = request.form['value1']
            value2 = request.form['value2']
            try:
                value1 = float(value1)
                value2 = float(value2)
                print('The variable a number')
            except:
                print('The variable is not a number')
                flash("You must enter a number!")
                return render_template("calculator.html")
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            result = getattr(Calculator, operation)(my_tuple)
            Calculations.add_calculation_to_history(int(time.time()),value1, value2, operation)
            # data = Calculations.get_calc_result_history()
            # Need double square brackets or will get a "shape" error
            Filehandler.write_vals_to_csv([[int(time.time()),value1, value2, operation]])
            # Need the result!!!
            data = Filehandler.get_csv_result_history()
            # print("data: " + str(data))
            if result == 'DivBy0':
                flash("Divide by Zero is UNDEFINED")
            len_data = len(data)
            print("result = " + str(result))
            return render_template('result.html', len_data=len_data, data=data,
                                   value1=value1, value2=value2, operation=operation, result=result)

        flash("You must enter a value for BOTH value 1 and value 2")
        return render_template('calculator.html')

    @staticmethod
    def get():
        """ Get Blank form """
        return render_template('calculator.html')
