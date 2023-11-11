rom flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    global numbers
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    return render_template("index.html", numbers=numbers)

@app.route("/count", methods=["POST"])
def count():
    global numbers
    number = numbers.pop(0)
    return "Count: {}".format(number)


"""@app.route("/")
def index():
    global number
    number = 1
    return render_template("index.html", number=number)

@app.route("/count", methods=["POST"])
def count():
    global number
    number += 1
    return "Count: {}".format(number)
"""
def timer():
    while True:
        time.sleep(1)
        request.get("/count")

if __name__ == "__main__":
    app.run(debug=True)



