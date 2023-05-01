from flask import Flask, render_template, request, jsonify
import time
import threading

app = Flask(__name__)

# Define a global variable to store the current number
current_number = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global current_number
    current_number = int(request.form['number'])
    return jsonify({'success': True})

@app.route('/get_number')
def get_number():
    global current_number
    while current_number < 100:
        current_number += 1
        time.sleep(1)
        return jsonify({'number': current_number})

if __name__ == '__main__':
    app.run(debug=True)
    #thread = threading.Thread(target=get_number)
    #thread.start()