#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()
app.config.from_object(config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match languagr with our supported languages"""
    # Check for 'locale' argument in URL query string
    locale = request.args.get('locale')
    if locale in config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(config.LANGUAGES)


@app.route('/')
def home() -> str:
    """returns a simple index page"""
    home_title = _("home_title")
    home_header = _("home_header")
    current_locale = get_locale()
    return render_template('4-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           current_locale=current_locale)


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
