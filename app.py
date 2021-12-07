from flask import Flask, render_template, flash


app = Flask(__name__)
app.secret_key = "My_Secret_ key"

@app.route('/')
def hello_world():  # put application's code here
    flash("flash test!!!!")
    return render_template("flash_msgs.html")


if __name__ == '__main__':
    app.run()
