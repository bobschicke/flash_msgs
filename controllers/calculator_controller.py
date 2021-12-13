import time
from history.calculations import Calculations
from calculator.calculator import Calculator
from csv_util.file_utils import Filehandler
from flask import render_template, request, flash, redirect, url_for, session
from csv_util.file_utils import Filehandler


class CalculatorController:
    @staticmethod
    def post():
        """ Get data and post values to form """
        #if request.form['delete_history'] == 'delete_history':
            #print('delete history')

        if request.form['value1'] != '' and request.form['value2'] != '':
            # get the values out of the form
            # todo test for nan
            value1 = float(request.form['value1'])
            value2 = float(request.form['value2'])
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
            #print("data: " + str(data))

            len_data = len(data)
            return render_template('result.html', len_data=len_data, data=data,
                                   value1=value1, value2=value2, operation=operation, result=result)

        flash("You must enter a value for BOTH value 1 and value 2")
        error = 'You must enter a value for value 1 and or value 2'
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """ Get Blank form """
        return render_template('calculator.html')








