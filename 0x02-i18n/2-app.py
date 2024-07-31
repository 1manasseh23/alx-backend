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


def create_app():
    """create flask"""

    app = Flask(__name__)

    # Initialize Babel with the Flask app
    babel.init_app(app)

    @app.route('/')
    def index():
        """Return 2-index.html"""

        return render_template('2-index.html')

    @babel.localeselector
    def get_locale():

        # Get the best match with the supported languages
        return request.accept_languages.best_match(["en", "fr"])

    return app


if __name__ == "__main__":
    """Run the app"""
    app = create_app()
    app.run(debug=True)
