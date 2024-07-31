#!/usr/bin/env python3
"""Flask application with Babel for internationalization.

This module sets up a basic Flask application with internationalization
support using Flask-Babel. It allows forcing a locale via a URL parameter and
falls back to the best match from the `Accept-Language` header if the
parameter is not present.
"""

from flask import Flask, request, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Select the best language match from the supported languages.

    Checks for a `locale` parameter in the request arguments. If present
    and supported, uses it as the locale. Otherwise, falls back to the
    `Accept-Language` header to determine the best language match
    among the supported locales.

    Returns:
        str: The selected locale code.
    """
    # Check if 'locale' parameter is in the URL query string
    locale_param = request.args.get('locale')
    if locale_param in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale_param
    # Fallback to the `Accept-Language` header
    return request.accept_languages.best_match(
        app.config['BABEL_SUPPORTED_LOCALES']
    )


@app.route('/')
def index() -> str:
    """Render the index page.

    This route renders the index page using the appropriate locale, which
    can be determined from the `locale` URL parameter or
    the `Accept-Language` header.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
