from flask import Flask, render_template, flash


app = Flask(__name__)
app.secret_key = "My_Secret_key"


@app.route('/')
def flash_test():  # put application's code here
    flash("Welcome to my Flash Test!")

    return render_template("flash_msgs.html")


@app.route('/internet_history')
def internet_history_get():
    return render_template("internet_history.html")

@app.route('/calculator', methods=["GET"])
def calculator_get():
    return render_template("calculator.html")

@app.route('/calculator', methods=["POST"])
def calculator_post():
    return render_template("calculator.html")


if __name__ == '__main__':
    app.run()
