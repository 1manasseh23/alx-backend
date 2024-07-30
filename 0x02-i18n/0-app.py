#!/usr/bin/env python3
"""This  a basic Flask app"""
from app import app
from flask import Flask, render_template

# app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
