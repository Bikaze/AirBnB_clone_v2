#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and Routes: /: display “Hello HBNB!”"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This function implements for the route '/'"""
    return "Hello HBNB!"


app.run(host="0.0.0.0", port=5000)
