#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and Routes: /cities_by_states: display a HTML page"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """This function implements for the route '/cities_by_states'"""
    states_all = storage.all("State")
    return render_template("8-cities_by_states.html", states=states_all)


@app.teardown_appcontext
def teardown(e):
    """This function removes the current Storage(db or file) Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
