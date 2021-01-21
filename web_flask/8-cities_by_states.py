#!/usr/bin/python3
"""start a flask app"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states/', strict_slashes=False)
def cityls():
    db = storage.all(State).values()
    return render_template('8-cities_by_states.html', db=db)


@app.teardown_appcontext
def close_db(err):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
