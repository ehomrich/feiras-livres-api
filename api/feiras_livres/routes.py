from flask import request, jsonify

from api.extensions import db
from api.feiras_livres import blueprint
from api.feiras_livres.models import Distrito, Feira
from api.feiras_livres.schemas import FeiraSchema

READONLY_PROPERTIES = ('id', 'registro', 'distrito', 'subprefeitura',)
SIMPLE_QS_FILTERS = ('regiao5', 'nome_feira', 'bairro',)


@blueprint.route('/', methods=['POST'])
def create():
    payload = request.get_json(force=True)

    instance = Feira(**payload)
    db.session.add(instance)
    db.session.commit()

    schema = FeiraSchema()
    return jsonify(schema.dump(instance))


@blueprint.route('/<registro>', methods=['DELETE'])
def delete(registro):
    instance = Feira.query.filter_by(registro=registro).first_or_404()

    db.session.delete(instance)
    db.session.commit()

    schema = FeiraSchema()
    return jsonify(schema.dump(instance))


@blueprint.route('/<registro>', methods=['PUT'])
def update(registro):
    payload = request.get_json(force=True)

    for prop in READONLY_PROPERTIES:
        payload.pop(prop)

    instance = Feira.query.filter_by(registro=registro).first_or_404()

    for key, value in payload.items():
        setattr(instance, key, value)

    db.session.commit()

    schema = FeiraSchema()
    return jsonify(schema.dump(instance))


@blueprint.route('/', methods=['GET'])
def get():
    querystring = {key: value for key, value in request.args.items() if key in SIMPLE_QS_FILTERS}
    related_param = request.args.get('distrito', None)

    query = Feira.query.filter_by(**querystring).join('subprefeitura').join('distrito')

    if related_param is not None:
        query = query.filter(Distrito.nome == related_param)

    result = query.all()

    schema = FeiraSchema()
    return jsonify(schema.dump(result, many=True))
