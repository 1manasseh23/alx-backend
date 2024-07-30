#!/usr/bin/env python3
"""This  a basic Flask app"""
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('0-index.html')
