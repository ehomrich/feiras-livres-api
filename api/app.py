from flask import Flask

from api.extensions import db, migrate, marshmallow
from api import commands
from api.feiras_livres import blueprint as feiras_livres_bp
from api.feiras_livres.models import Distrito, Subprefeitura, Feira


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.AppConfig')

    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)
    register_commands(app)
    register_error_handlers(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)


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
    app.register_blueprint(feiras_livres_bp)


def register_commands(app):
    app.cli.add_command(commands.import_data)


def register_error_handlers(app):
    pass
