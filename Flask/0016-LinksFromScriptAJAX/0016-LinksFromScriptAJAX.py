from flask import Flask, jsonify, render_template
from links import links_spit

app = Flask(__name__) 

links = []

@app.route('/')
def index():
    return render_template('index.html', links=links)

'''@app.route('/get_link')
def get_links():
    link = next(links_spit())
    links.append(link)
    return jsonify({'link': link})'''

'''@app.route('/get_link')
def get_links():
    for link in links_spit():
        links.append(link)
    return jsonify({'links': links})'''

@app.route('/get_link')
def get_links():
    links.append(links_spit())
    return jsonify({'links': links})
    

'''@app.route('/get_link')
def get_links():
    links = []
    for link in links_spit():
        links.append(link)
    return jsonify({'links': links})'''
    
'''@app.route('/get_link')
def get_links():
    def generate_links():
        for link in links_spit():
            yield link
            links.append(link)
    
    return Response(generate_links(), mimetype='text/event-stream')'''


'''@app.route('/get_link')
def get_links():
    # Use a generator expression to yield links one by one
    links_gen = links_spit()
    for i in range(len(links)):
        try:
            # Try to get the next link from the generator expression
            link = next(links_gen)
            links.append(link)
        except StopIteration:
            # If there are no more links to yield, break out of the loop
            break
    return jsonify({'links': links})'''




if __name__ == '__main__':
    app.run(debug=True)