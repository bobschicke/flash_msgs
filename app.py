from flask import Flask, render_template, flash
from controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication
from controllers.result_controller import ResultController

app = Flask(__name__)
app.secret_key = "My_Secret_key"
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route('/')
def flash_test():  # put application's code here
    flash("Welcome to my Flash Message Demo!.....Click on the X to close the message....Refresh the page to get me back!")
    return render_template("flash_msgs.html")


@app.route('/internet_history', methods=["GET"])
def internet_history_get():
    return render_template("internet_history.html")


@app.route('/calculator', methods=["GET"])
def calculator_get():
    print('calculator_get')
    return CalculatorController.get()


@app.route('/calculator', methods=["POST"])
def calculator_post():
    print('calculator_post')
    return CalculatorController.post()


@app.route('/result', methods=["GET"])
def result_get():
    print('result_get')
    return ResultController.get()


@app.route('/result', methods=["POST"])
def result_post():
    # flash("History Was Deleted!")
    print('result_post')
    return ResultController.post()

@app.route('/calc_oop_grid')
def calc_oop_grid():  # put application's code here
    return render_template("calc_oop_grid.html")

@app.route('/calc_oop')
def calc_oop():  # put application's code here
    return render_template("calc_oop.html")


if __name__ == '__main__':
    app.run()
