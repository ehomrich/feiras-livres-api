from flask import Flask

from api.extensions import db, migrate
from api.feiras_livres.models import Distrito, Subprefeitura, Feira


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.AppConfig')

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)
    register_error_handlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_shell_context(app):
    @app.shell_context_processor
    def db_context():
        return {
            'db': db,
            'Distrito': Distrito,
            'Subprefeitura': Subprefeitura,
            'Feira': Feira
        }


def register_blueprints(app):
    pass


def register_error_handlers(app):
    pass
