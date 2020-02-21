from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.AppConfig')

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    pass


def register_error_handlers(app):
    pass
