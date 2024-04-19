#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and implements Routes: /, and /hbnb"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This function implements for the route '/'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    """This function implements for the route '/hbnb'"""
    return "HBNB"


app.run(host="0.0.0.0", port=5000)
