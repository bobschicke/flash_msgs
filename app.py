"""This is the "main" file"""
from werkzeug.debug import DebuggedApplication
from flask import Flask, render_template, flash
from controllers.calculator_controller import CalculatorController
from controllers.result_controller import ResultController

app = Flask(__name__)
app.secret_key = "My_Secret_key"
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route('/')
def flash_test():
    """This loads the flash test page"""
    flash("Welcome to my Flash Message Demo!.....Click on the X to close the message"
          "....Refresh the page to get me back!")
    return render_template("flash_msgs.html")


@app.route('/calculator', methods=["GET"])
def calculator_get():
    """This loads the calculator page"""
    print('calculator_get')
    return CalculatorController.get()


@app.route('/calculator', methods=["POST"])
def calculator_post():
    """This handles a calculator post"""
    print('calculator_post')
    return CalculatorController.post()


@app.route('/result', methods=["GET"])
def result_get():
    """This loads the result page"""
    print('result_get')
    return ResultController.get()


@app.route('/result', methods=["POST"])
def result_post():
    """This loads the result page"""
    # flash("History Was Deleted!")
    print('result_post')
    return ResultController.post()


@app.route('/calc_oop_grid')
def calc_oop_grid():  # put application's code here
    """This loads the calc oop page"""
    return render_template("calc_oop_grid.html")


@app.route('/aaa_testing_grid')
def aaa_testing_grid():  # put application's code here
    """This loads the aaa testing page"""
    return render_template("aaa_testing_grid.html")


@app.route('/pylint_oop_grid')
def pylint_oop_grid():  # put application's code here
    """This loads the pylint page"""
    return render_template("pylint_oop_grid.html")


@app.route('/solid_grid')
def solid_grid():  # put application's code here
    """This loads the solid page"""
    return render_template("solid_grid.html")


if __name__ == '__main__':
    app.run()
