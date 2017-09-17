# _*_ coding: utf-8 _*_

from flask import Flask


def create_app(config=None):
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

    from .main import main
    app.register_blueprint(main)

    return app
