#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and implements Routes: /, /hbnb, /c/<text>, /python/,
 and /python/<text>"""

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
def variable_rule_c(text):
    """This function implements for the route '/c/<text>'"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def variable_rule_py(text="is cool"):
    """This function implements for the route '/python/<text>'"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
