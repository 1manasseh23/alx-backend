#!/usr/bin/env python3
"""This  a user login system is outside the scope of this project
To emulate a similar behavior"""
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
        return render_template('5-index.html')

    @babel.localeselector
    def get_locale():
        # Check if locale is provided in URL parameters
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
        # Fallback to the best match with the supported languages
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    def get_user():
        user_id = request.args.get('login_as')
        if user_id and user_id.isdigit():
            user_id = int(user_id)
            return users.get(user_id)
        return None

    @app.before_request
    def before_request():
        g.user = get_user()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
