from flask import Flask, render_template, flash


app = Flask(__name__)
app.secret_key = "My_Secret_key"

@app.route('/')
def flash_test():  # put application's code here
    flash("Welcome to my Flash Test!")
    return render_template("flash_msgs.html")


if __name__ == '__main__':
    app.run()
