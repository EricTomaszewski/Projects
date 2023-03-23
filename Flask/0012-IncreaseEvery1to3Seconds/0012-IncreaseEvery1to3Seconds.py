from flask import Flask, jsonify, render_template
import random
import time

app = Flask(__name__)

number = 1

def update_number():
    global number
    while True:
        time.sleep(random.uniform(1, 3))
        # time.sleep(1)
        number = (number % 10) + 1

@app.route('/')
def index():
    return render_template('index.html', number=number)

@app.route('/get_number')
def get_number():
    return jsonify({'number': number})

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_number)
    t.start()
    app.run(debug=True)
