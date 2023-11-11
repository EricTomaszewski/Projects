'''from flask import Flask, render_template, request, jsonify
import time
import threading
import subprocess
from links import number_spit

app = Flask(__name__)

# Define a global variable to store the current number
current_number = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global current_number
    global process
    current_number = int(request.form['number'])
    process = subprocess.Popen(['python', 'links.py', str(current_number)], stdout=subprocess.PIPE)
    return jsonify({'success': True})

@app.route('/get_number')
def get_number():
    global current_number
    global process
    output_bytes = process.stdout.read()
    current_number = output_bytes.decode('utf-8', errors='replace').strip()         # before it was 'output'
    return jsonify({'number': current_number})

if __name__ == '__main__':
    app.run(debug=True)
    thread = threading.Thread(target=get_number)
    thread.start()'''
    
    
    
'''from flask import Flask, request, jsonify, render_template
from subprocess import Popen, PIPE
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    number = request.form.get('number')
    process = Popen(['python', 'links.py', number], stdout=PIPE, stderr=PIPE)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/get_number', methods=['GET'])
def get_number():
    # process = Popen(['tail', '-n', '1', 'output.txt'], stdout=PIPE, stderr=PIPE)                         # Unix
    process = Popen(['cmd', '/c', 'type output.txt | findstr /B /E /C:""'], stdout=PIPE, stderr=PIPE)       # Windows

    output, err = process.communicate()
    if err:
        return json.dumps({'error': err.decode('utf-8')}), 500, {'ContentType': 'application/json'}
    else:
        number = int(output.decode('utf-8').strip())
        return json.dumps({'number': number}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)'''






    
    
    

from flask import Flask, render_template, jsonify, request
from subprocess import Popen, PIPE
import sys
from links import number_spit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    number = request.form['number']
    process = Popen(['python', 'links.py', number], stdout=PIPE, stderr=PIPE)
    return 'Success'

@app.route('/get_number', methods=['GET'])
def get_number():
    process = Popen(['python', 'links.py'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
    output, error = process.communicate()
    if output:
        number = int(output.decode('utf-8'))
        return jsonify({'number': number})
    else:
        return jsonify({'error': error.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)

