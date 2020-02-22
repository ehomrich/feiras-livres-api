from flask import request, jsonify
from werkzeug.exceptions import NotFound

from api.extensions import db
from api.feiras_livres import blueprint
from api.feiras_livres.models import Distrito, Subprefeitura, Feira
from api.feiras_livres.schemas import FeiraSchema, CreateFeiraSchema, UpdateFeiraSchema

READONLY_PROPERTIES = ('id', 'registro', 'distrito', 'subprefeitura',)
SIMPLE_QS_FILTERS = ('regiao5', 'nome_feira', 'bairro',)


@blueprint.route('/', methods=['POST'])
def create():
    payload = request.get_json(force=True)

    create_schema = CreateFeiraSchema()
    errors = create_schema.validate(payload)

    if errors:
        return jsonify(errors), 400

    try:
        distrito = Distrito.query.get_or_404(payload['codigo_distrito'])
        subprefeitura = Subprefeitura.query.get_or_404(payload['codigo_subprefeitura'])

        feira = Feira(**payload)

        db.session.add(feira)
        db.session.commit()

        schema = FeiraSchema()
        return jsonify(schema.dump(feira))
    except NotFound:
        return jsonify(message='Distrito e/ou subprefeitura não encontrados'), 404


@blueprint.route('/<registro>', methods=['DELETE'])
def delete(registro):
    try:
        feira = Feira.query.filter_by(registro=registro).join('subprefeitura').join('distrito').first_or_404()

        schema = FeiraSchema()
        dump = schema.dump(feira)

        db.session.delete(feira)
        db.session.commit()

        schema = FeiraSchema()
        return jsonify(dump)
    except NotFound:
        return jsonify(message='Feira não encontrada'), 404


@blueprint.route('/<registro>', methods=['PUT'])
def update(registro):
    payload = request.get_json(force=True)

    for prop in READONLY_PROPERTIES:
        payload.pop(prop, None)

    update_schema = UpdateFeiraSchema()
    errors = update_schema.validate(payload)

    if errors:
        return jsonify(errors), 400

    try:
        distrito = Distrito.query.get_or_404(payload['codigo_distrito'])
        subprefeitura = Subprefeitura.query.get_or_404(payload['codigo_subprefeitura'])

        feira = Feira.query.filter_by(registro=registro).first_or_404()

        for key, value in payload.items():
            setattr(feira, key, value)

        db.session.commit()

        schema = FeiraSchema()
        return jsonify(schema.dump(feira))
    except NotFound:
        return jsonify(message='Distrito e/ou subprefeitura não encontrados'), 404


@blueprint.route('/', methods=['GET'])
def get():
    querystring = {key: value for key, value in request.args.items() if key in SIMPLE_QS_FILTERS}
    related_param = request.args.get('distrito', None)

    query = Feira.query.filter_by(**querystring).join('subprefeitura').join('distrito')

    if related_param is not None:
        query = query.filter(Distrito.nome == related_param)

    results = query.all()

    schema = FeiraSchema()
    return jsonify(schema.dump(results, many=True))
