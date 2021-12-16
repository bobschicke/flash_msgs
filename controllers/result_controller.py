"""This is the Result Controller file"""
from flask import request, flash
from controllers.calculator_controller import CalculatorController
from csv_util.file_utils import Filehandler


class ResultController:
    """This is the Result Controller Class"""
    @staticmethod
    def post():
        """ Get data and post values to form """
        print("post")
        if request.form['delete_history'] == 'Delete History File':
            print("Button pressed")
            Filehandler.delete_history()
            flash("The History Has Been Deleted!")
        return CalculatorController.get()

    @staticmethod
    def get():
        """This is the Result Controller get method"""
        # print("get")
