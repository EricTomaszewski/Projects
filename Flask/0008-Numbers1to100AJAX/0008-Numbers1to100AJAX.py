from flask import Flask, jsonify, render_template
import threading
import time

app = Flask(__name__)

numbers = []

def update_numbers():
    global numbers
    for i in range(1, 101):
        numbers.append(i)
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html', numbers=numbers)

@app.route('/get_numbers')
def get_numbers():
    return jsonify({'numbers': numbers})

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_numbers)
    t.start()
    app.run(debug=True)
