# app.py

'''
https://realpython.com/flask-connexion-rest-api/

'''

'''
Action	HTTP Verb	URL Path	Description
Read	GET	/api/people	Read a collection of people.
Create	POST	/api/people	Create a new person.
Read	GET	/api/people/<lname>	Read a particular person.
Update	PUT	/api/people/<lname>	Update an existing person.
Delete	DELETE	/api/people/<lname>	Delete an existing person.
'''

from flask import render_template   # , Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")
# app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)