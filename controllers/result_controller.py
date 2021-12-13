import os
import time
from controllers.calculator_controller import CalculatorController
from history.calculations import Calculations
from calculator.calculator import Calculator
from csv_util.file_utils import Filehandler
from flask import render_template, request, flash, redirect, url_for, session
from csv_util.file_utils import Filehandler



class ResultController:
    @staticmethod
    def post():
        """ Get data and post values to form """
        print("post")
        if request.form['delete_history'] == 'delete_history':
            print("Button pressed")
            Filehandler.delete_history()
            flash("The History Has Been Deleted!")
        return CalculatorController.get()

    @staticmethod
    def get():
        print("get")