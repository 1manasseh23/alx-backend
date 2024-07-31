#!/usr/bin/env python3
"""
This a get_locale function with the babel.localeselector
decorator. Use request.accept_languages to determine the
best match with our supported languages
"""
from flask import Flask, render_template, request
from flask_babel import Babel

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
        """Return 2-index.html"""

        return render_template('2-index.html')

    @babel.localeselector
    def get_locale():

        # Get the best match with the supported languages
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
