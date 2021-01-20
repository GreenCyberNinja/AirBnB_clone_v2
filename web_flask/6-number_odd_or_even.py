#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_(text):
    """returns c and text/ convert _ to whitespace"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_(text="is cool"):
    """returns python and text, text default is ,is cool,"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """returns n is a number if n is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """displays an html page if n is number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def od_ven(n):
    """displays if n is even or odd"""
    if n % 2 is 0:
        return render_template('6-number_odd_or_even.html', n=n, eo="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, eo="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
