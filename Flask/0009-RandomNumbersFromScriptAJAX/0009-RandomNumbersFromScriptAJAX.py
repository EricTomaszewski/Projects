from flask import Flask, jsonify, render_template
from random_number import generate_random_number

app = Flask(__name__)

numbers = []

@app.route('/')
def index():
    return render_template('index.html', numbers=numbers)

@app.route('/get_random_number')
def get_random_number():
    number = generate_random_number()
    numbers.append(number)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True)