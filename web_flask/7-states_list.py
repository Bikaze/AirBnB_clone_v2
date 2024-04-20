#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and Routes: /states_list: display a HTML page"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """This function implements for the route '/states_list'"""
    states_all = storage.all("State")
    return render_template("7-states_list.html", states=states_all)


@app.teardown_appcontext
def teardown(e):
    """This function removes the current Storage(db or file) Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
