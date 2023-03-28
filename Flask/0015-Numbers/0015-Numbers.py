'''from flask import Flask, render_template
from numb import func

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', numbers=func())

if __name__ == '__main__':
    app.run(debug=True)'''
    

from flask import Flask, render_template, jsonify
from threading import Thread
import time

app = Flask(__name__)

def func():
    for i in range(1000000):
        time.sleep(1)
        yield i

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numbers')
def numbers():
    return jsonify(list(func()))

if __name__ == '__main__':
    Thread(target=func).start()
    app.run(debug=True)

