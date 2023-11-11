from flask import Flask, render_template, Response, jsonify
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

  
  
process = Popen(['python', '-u', 'random_generator.py'], stdout=PIPE, bufsize=1, universal_newlines=True)
@app.route('/values')
def values():
    for line in iter(process.stdout.readline, ''):
        value = line.rstrip() #+ '<br>'
        print(value)  # Print value in the terminal
        # yield value
        # output = str(value)
        output = value
        return jsonify({'output': output})
        # return value

#    return Response(generate_values(), mimetype='text/html')
      # Generate some output
    
  

'''        output_bytes = process.stdout.read()
        # Decode the byte string and format the result
        output = output_bytes.decode().strip()
        
        
        # Return the result as a plain text response
        return output + " " + str(output2)'''


if __name__ == '__main__':
    app.run(debug=True)
