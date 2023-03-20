from flask import Flask, render_template, request, Response
import subprocess

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def calculate():
    if request.method == "POST":
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
        
        # Return the result as a plain text response
        return output + " " + str(output2)
        # rather than which would render new html page:
        # return render_template('result.html', result=[output,output2])
    else:
        return render_template('index.html')
    
    
    
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
    
    
    
    

'''
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
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
    
    # Return the result as a plain text response
    return output + " " + str(output2)
    # rather than which would render new html page:
    # return render_template('result.html', result=[output,output2])
'''