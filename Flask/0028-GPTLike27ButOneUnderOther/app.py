from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_updates')
def get_updates():
    # Simulate long-running process
    time.sleep(1)

    # Generate some output
    output = 'Real-time update: ' + str(time.time())

    return jsonify({'output': output})


if __name__ == '__main__':
    app.run(debug=True)


