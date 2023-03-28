from flask import Flask, jsonify, render_template
from links import links_spit

app = Flask(__name__) 

links = []

@app.route('/')
def index():
    return render_template('index.html', links=links)


### prints a single letter per line
'''@app.route('/get_link')
def get_links():
    for link in links_spit():
        links.append(link)
    return jsonify({'links': links})'''

@app.route('/get_link')
def get_links():
    links.append(links_spit())
    return jsonify({'links': links})



if __name__ == '__main__':
    app.run(debug=True)