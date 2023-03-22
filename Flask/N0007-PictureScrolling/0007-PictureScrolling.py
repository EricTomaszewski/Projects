    
from flask import Flask, render_template
import os

app = Flask(__name__)

# specify the directory containing image files
# IMAGE_DIR = r'C:\Users\irene\!PROJECTS\Flask\0007-PictureScrolling\static\pictures'
IMAGE_DIR = './static/pictures/'

@app.route('/')
def index():
    # get all image files in the directory
    image_files = [os.path.join(IMAGE_DIR, f) for f in os.listdir(IMAGE_DIR) if f.endswith('.jpg') or f.endswith('.png')]
    return render_template('index.html', image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)

