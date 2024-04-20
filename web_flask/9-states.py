#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and Routes: /states: and /states/<id>,
then display a HTML page"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state_id(id=None):
    """This function implements for the route '/states/<id>"""
    states_all = storage.all("State")
    if id:
        for state in states_all.values():
            if state.id == id:
                return render_template("9-states.html", states=state, sid=id)
        else:
            return render_template("9-states.html")
    return render_template("9-states.html", states=states_all)


@app.teardown_appcontext
def teardown(e):
    """This function removes the current Storage(db or file) Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
