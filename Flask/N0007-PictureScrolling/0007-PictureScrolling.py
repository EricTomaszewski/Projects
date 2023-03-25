import os
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

images_dir = 'static/images'
image_names = os.listdir(images_dir)
image_count = len(image_names)
current_image_index = 0

@app.route('/')
def index():
    return render_template('index.html', image_names=image_names)

@app.route('/get_next_image')
def get_next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % image_count
    return jsonify({'image_url': f'static/images/{image_names[current_image_index]}'})
    
if __name__ == '__main__':
    app.run(debug=True)





'''
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the list of pictures from the folder
    pic_list = os.listdir('static/pictures')
    # Render the index.html template with the list of pictures
    return render_template('index.html', pic_list=pic_list)

if __name__ == '__main__':
    app.run(debug=True)






<!DOCTYPE html>
<html>
<head>
    <title>Picture Gallery</title>
    <style>
        .pic-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50vh;
            margin-top: 20px;
        }
        .pic-container img {
            width: 50%;
            height: auto;
            margin: 0 auto;
        }
        .btn-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        button {
            margin: 0 10px;
        }
    </style>
</head>
<body>
    {% if pic_list %}
    <div class="pic-container">
        <img src="{{ url_for('static', filename='pictures/' + pic_list[0]) }}" id="pic">
    </div>
    <div class="btn-container">
        <button id="prev-btn" onclick="prevImage()">Previous</button>
        <button id="next-btn" onclick="nextImage()">Next</button>
    </div>
    {% endif %}
    <script>
        var index = 0;
        var picList = JSON.parse('{{ pic_list | tojson | safe }}');

        function nextImage() {
            index = (index + 1) % picList.length;
            document.getElementById('pic').src = '{{ url_for('static', filename='pictures/') }}' + picList[index];
        }

        function prevImage() {
            index = (index - 1 + picList.length) % picList.length;
            document.getElementById('pic').src = '{{ url_for('static', filename='pictures/') }}' + picList[index];
        }

        setInterval(nextImage, 2000);
    </script>
</body>
</html>

'''