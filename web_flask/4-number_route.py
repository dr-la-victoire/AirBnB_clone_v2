#!/usr/bin/python3
"""This module starts up a Flask application"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Displays a custom text"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays another custom text"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cee(text):
    """Displays a dynamic text beginning with C"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays a dynamic text beginning with Python"""
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """Displays a dynamic text only if n is a number"""
    if isinstance(n, int):
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)