#!/usr/bin/python3
"""This is a script that starts a Flask web application: listening on
0.0.0.0, port 5000, and Routes: /hbnb_filters: display a HTML page"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """This function implements for the route '/hbnb_filters'"""
    states_all = storage.all("State")
    amenities_all = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states_all, amenities=amenities_all)


@app.teardown_appcontext
def teardown(e):
    """This function removes the current Storage(db or file) Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
