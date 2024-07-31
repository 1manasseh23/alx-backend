#!/usr/bin/python3
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr', 'es']

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(
            app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    """Render the index page."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
