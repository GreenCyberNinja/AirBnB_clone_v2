#!/usr/bin/python3
"""start a flask app"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def statels():
    db = storage.all(State).values()
    return render_template('7-states_list.html', db=db)


@app.route('/states/<id>', strict_slashes=False)
def statebyid(id):
    """gets the state by id"""
    stls = storage.all(State)
    stid = 'State.{}'.format(id)
    if stid in stls:
        stls = stls[stid]
    else:
        stls = None
    return render_template('9-states.html', stls=stls)


@app.teardown_appcontext
def close_db(err):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
