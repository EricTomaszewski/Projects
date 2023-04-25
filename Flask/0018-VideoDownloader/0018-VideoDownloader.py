from flask import Flask, render_template, request, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def calculate():
    VideoLink = request.form['VideoLink']
    
    # EXTERNAL SCRIPT
    # Call the external Python script and capture its multiplication output
    process = subprocess.Popen(['python', 'VideoDownloaderScript.py', str(VideoLink)], stdout=subprocess.PIPE)
    output_bytes = process.stdout.read()
    # Decode the byte string and format the result
    output = output_bytes.decode().strip()
    
    # INTERNAL FLASK
    # and here the sum without using the script
    # output2 = a + b
    
    # Return the result as a plain text response
    return output # + " " + str(output2)
    # rather than which would render new html page:
    # return render_template('result.html', result=[output,output2])


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()