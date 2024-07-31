#!/usr/bin/env python3
"""This is Based on the inferred time zone, display the
current time on the home page in the default format. For example:
Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError
from datetime import datetime

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
        # Get current time in the inferred timezone
        tz = get_timezone()
        now = datetime.now(pytz.timezone(tz))
        # Format time according to locale
        current_time = format_datetime(now)
        return render_template('8-index.html', current_time=current_time)

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

    @babel.timezoneselector
    def get_timezone():
        # 1. Check if timezone is provided in URL parameters
        timezone = request.args.get('timezone')
        if timezone:
            try:
                pytz.timezone(timezone)
                return timezone
            except UnknownTimeZoneError:
                pass

        # 2. Check if user is logged in and use their timezone
        if g.user and g.user['timezone']:
            try:
                pytz.timezone(g.user['timezone'])
                return g.user['timezone']
            except UnknownTimeZoneError:
                pass

        # 3. Default to UTC
        return app.config['BABEL_DEFAULT_TIMEZONE']

    @app.before_request
    def before_request():
        g.user = get_user()

    def get_user():
        user_id = request.args.get('login_as')
        if user_id and user_id.isdigit():
            user_id = int(user_id)
            return users.get(user_id)
        return None

    def format_datetime(dt):
        # Format date and time based on the current locale
        return babel.dates.format_datetime(dt, format='full')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
