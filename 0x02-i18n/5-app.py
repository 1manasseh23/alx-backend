#!/usr/bin/env python3
"""Flask application with Babel for internationalization
and user login emulation.

This module sets up a basic Flask application with internationalization
support using Flask-Babel. It emulates user login by using a mock user
database and  displays user-specific messages based on
the `login_as` URL parameter.
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Retrieve user data based on the `login_as` URL parameter.

    Checks the `login_as` parameter in the request arguments and
    returns the user data if the user ID is valid. If the parameter
    is not present or the ID is not
    valid, returns None.

    Returns:
        dict: The user dictionary or None if not found.
    """

    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Set the user in Flask's global context.

    Uses the `get_user` function to set the `g.user` global
    variable with the user data if available. This function
    runs before each request.
    """
    
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Select the best language match from the supported languages.

    Checks for a `locale` parameter in the request arguments. If
    present and supported, uses it as the locale. Otherwise, falls
    back to the `Accept-Language` header to determine the best
    language match among the supported locales.

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

    This route renders the index page using the appropriate locale
    and displays a user-specific message if a user is logged in.

    Returns:
        str: Rendered HTML content of the index page.
    """
    
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
