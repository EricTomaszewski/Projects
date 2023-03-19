from flask import Flask, render_template, request, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


'''@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = a + b
    return render_template('result.html', result=result)'''


@app.route('/calculate', methods=['POST'])
def calculate2():
    a = int(request.form['a'])
    b = int(request.form['b'])
    
    # EXTERNAL SCRIPT
    # Call the external Python script and capture its multiplication output
    process = subprocess.Popen(['python', 'MultiplyABScript.py', str(a), str(b)], stdout=subprocess.PIPE)
    output_bytes = process.stdout.read()
    # Decode the byte string and format the result
    output = output_bytes.decode().strip()
    
    # INTERNAL FLASK
    # and here the sum without using the script
    output2 = a + b
    
    return render_template('result.html', result=[output,output2])


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
    
    
    
    

'''
@app.route('/calculate', methods=['POST'])
def calculate():
    a = int(request.form['a'])
    b = int(request.form['b'])
    result = a + b
    return render_template('result.html', result=result)

@app.route('/calculate2', methods=['POST'])
def calculate2():
    a = int(request.form['a'])
    b = int(request.form['b'])
    # Call the external Python script and capture its output
    process = subprocess.Popen(['python', 'MultiplyABScript.py', str(a), str(b)], stdout=subprocess.PIPE)
    output = process.stdout.read()
    return render_template('result2.html', result=output)
'''