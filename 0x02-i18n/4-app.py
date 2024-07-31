#!/usr/bin/env python3
"""This a way to force a particular locale by passing the
locale=fr parameter to your app’s URLs"""
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
        return render_template('4-index.html')

    @babel.localeselector
    def get_locale():
        # Check if locale is provided in URL parameters
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
        # Fallback to the best match with the supported languages
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
