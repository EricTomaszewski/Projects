from flask import Flask, render_template
from random_phrase import get_random_phrase
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
  process = subprocess.Popen(["python", "random_phrase.py"], stdout=subprocess.PIPE)
  phrases = process.stdout.readlines()
  phrases = [phrase.decode("utf-8").strip() for phrase in phrases]
  return render_template("index.html", phrases=phrases)

if __name__ == "__main__":
  app.run(debug=True)
