#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)


def get_locale():
    supported_locales = ['fr', 'en']
    if 'locale' in request.args and request.args['locale'] \
            in supported_locales:
        return request.args['locale']
    else:
        # Fallback to default behavior
        return 'en'  # Default locale


@app.route('/')
def index():
    locale = get_locale()
    return f'<h1>Locale set to: {locale}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
