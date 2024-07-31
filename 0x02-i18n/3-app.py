#!/usr/bin/env python3
"""This the _ or gettext function to parametrize your
templates. Use the message IDs home_title and home_header"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

# Instantiate the Babel object
babel = Babel()


class Config:
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
        return render_template('3-index.html')

    @babel.localeselector
    def get_locale():
        # Get the best match with the supported languages
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
