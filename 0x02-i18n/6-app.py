#!/usr/bin/env python3
"""This get_locale function to use a user’s preferred
local if it is supported"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Instantiate the Babel object
babel = Babel()

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
        return render_template('6-index.html')

    @babel.localeselector
    def get_locale():
        # 1. Check if locale is provided in URL parameters
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

        # 2. Check if user is logged in and use their locale
        if g.user and g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']

        # 3. Fallback to the best match with the supported languages
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    return app


@app.before_request
def before_request():
    g.user = get_user()


def get_user():
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
