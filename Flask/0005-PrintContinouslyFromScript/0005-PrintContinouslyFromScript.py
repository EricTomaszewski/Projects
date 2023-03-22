from flask import Flask, render_template, request, jsonify
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/increment', methods=['POST'])
def increment():
    a = int(request.form['a'])
    b = int(request.form['b'])
    output = subprocess.Popen(['python', 'PrintContinously.py', str(a), str(b)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    '''for line in iter(output.stdout.readline, b''):
        time.sleep(1)
        yield jsonify({'number': int(line.decode().strip())})'''
    '''while True:
        next_line = output.stdout.readline().decode()
        if next_line == '' and output.poll() is not None:
            break
        time.sleep(1)
        yield jsonify({'number': int(next_line)})'''
    while True:
        next_line = output.stdout.read().decode().strip()
        if next_line == '' and output.poll() is not None:
            break
        yield jsonify({'number': int(next_line)})


if __name__ == '__main__':
    app.run(debug=True)





'''from flask import Flask, render_template, jsonify
import threading
import time
import subprocess

app = Flask(__name__)

a = 0
b = 0

def increment_values():
    global a, b
    while True:
        time.sleep(1)
        a += 1
        b += 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_values')
def get_values():
    global a, b
    result = subprocess.run(['python', 'increment.py', str(a), str(b)], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()
    a, b = map(int, output.split(','))
    return jsonify({'a': a, 'b': b})

if __name__ == '__main__':
    t = threading.Thread(target=increment_values)
    t.daemon = True
    t.start()
    app.run(debug=True)'''






'''from flask import Flask, render_template
import json
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Start the external script with a and b values as arguments
    p = subprocess.Popen(['python', 'external_script.py', str(a), str(b)], stdout=subprocess.PIPE)
    
    # Read the output of the external script line by line and send it to the client
    while True:
        line = p.stdout.readline()
        if not line:
            break
        data = json.dumps({'value': line.decode('utf-8').strip()})
        yield f"data: {data}\n\n"
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True)'''