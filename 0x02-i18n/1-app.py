#!/usr/bin/env python3
"""
This a instantiate the Babel object in your app
Store it in a module-level variable named babel
"""
from flask import Flask, render_template
from flask_babel import Babel

# Instantiate the Babel object
babel = Babel()


class Config:
    """Config to set Babel’s default
    locale ("en") and timezone ("UTC")"""
i
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Babel with the Flask app
    babel.init_app(app)

    @app.route('/')
    def index():
        """Return 1-index.html"""

        return render_template('1-index.html')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
