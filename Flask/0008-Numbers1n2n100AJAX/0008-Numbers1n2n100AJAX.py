from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    yield '1\n'
    time.sleep(1)
    yield '2\n'
    time.sleep(1)
    yield '100\n'

@app.route('/numbers')
def numbers():
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
