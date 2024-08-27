#!/usr/bin/env python3
"""Module 2"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


class Config:
    """Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index_2() -> str:
    """Displays the home page"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the client's preferred language"""
    supported_languages = app.config["LANGUAGES"]
    best_match = request.accept_languages.best_match(supported_languages)
    return best_match


if __name__ == "__main__":
    app.run(debug=True)
