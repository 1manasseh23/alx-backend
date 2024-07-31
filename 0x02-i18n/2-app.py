#!/usr/bin/env python3
"""Flask application with Babel for internationalization.

This module sets up a basic Flask application with internationalization support
using Flask-Babel. It configures the app to use different locales based on the
client's preferred language.
"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr', 'es']

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Select the best language match from the supported languages.

    Uses the `Accept-Language` header from the request to determine the best
    language match among the supported locales.

    Returns:
        str: The selected locale code.
    """
    return request.accept_languages.best_match(
        app.config['BABEL_SUPPORTED_LOCALES']
    )


@app.route('/')
def index() -> str:
    """Render the index page.

    This route renders the index page using the appropriate locale.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
