from flask import Flask, render_template, jsonify

app = Flask(__name__)

# This is a list of items that will be returned in chunks for infinite scrolling
items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']

# This variable keeps track of the current index into the list of items
current_index = 0

@app.route('/')
def index():
    # Render the initial page with the first set of items
    return render_template('index.html', items=items[:5])

@app.route('/load_more')
def load_more():
    global current_index
    # Increment the current index to load the next set of items
    current_index += 5
    # If we have reached the end of the list, reset the index to start over
    if current_index >= len(items):
        current_index = 0
    # Return the next set of items as JSON
    return jsonify(items=items[current_index:current_index+5])

if __name__ == '__main__':
    app.run(debug=True)
