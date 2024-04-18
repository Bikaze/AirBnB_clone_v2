#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and implements Routes: /, /hbnb, and /c/<text>"""

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


@app.route("/c/<text>", strict_slashes=False)
def variable_rule(text):
    """This function implements for the route '/c/<text>'"""
    return f"C {text.replace('_', ' ')}"


app.run(host="0.0.0.0", port=5000)
