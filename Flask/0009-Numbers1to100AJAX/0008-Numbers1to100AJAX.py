from flask import Flask, render_template, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    for i in range(100, 0, -1):
        yield str(i) + '\n'
        time.sleep(1)

@app.route('/numbers')
def numbers():
    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
