from flask import Flask

from api.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.AppConfig')

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    pass


def register_error_handlers(app):
    pass
