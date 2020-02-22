from flask import Blueprint

blueprint = Blueprint('feiras_livres', __name__, url_prefix='/feiras-livres')

from api.feiras_livres import routes