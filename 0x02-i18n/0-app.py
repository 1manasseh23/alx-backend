#!/usr/bin/env python3
"""This  a basic Flask app"""
from app import app
from flask import Flask, render_template


@app.route('/')
@app.route('/index')
def index():
    """Retun 0-index.html"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
