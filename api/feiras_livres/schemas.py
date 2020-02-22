from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from marshmallow import Schema, fields

from api.feiras_livres.models import Distrito, Subprefeitura, Feira


class DistritoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Distrito
        include_relationships = False


class SubprefeituraSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subprefeitura
        include_relationships = False


class FeiraSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Feira
        include_fk = False
        include_relationships = True

    distrito = Nested(DistritoSchema)
    subprefeitura = Nested(SubprefeituraSchema)


class CreateFeiraSchema(Schema):
    registro = fields.Str(required=True)
    nome_feira = fields.Str(required=True)
    setor_censitario = fields.Str(required=True)
    area_ponderacao = fields.Str(required=True)
    codigo_distrito = fields.Int(required=True)
    codigo_subprefeitura = fields.Int(required=True)
    regiao5 = fields.Str(required=True)
    regiao8 = fields.Str(required=True)
    logradouro = fields.Str(required=True)
    numero = fields.Str(required=False)
    bairro = fields.Str(required=True)
    referencia = fields.Str(required=False)
    latitude = fields.Str(required=True)
    longitude = fields.Str(required=True)

class UpdateFeiraSchema(Schema):
    nome_feira = fields.Str()
    setor_censitario = fields.Str()
    area_ponderacao = fields.Str()
    codigo_distrito = fields.Int()
    codigo_subprefeitura = fields.Int()
    regiao5 = fields.Str()
    regiao8 = fields.Str()
    logradouro = fields.Str()
    numero = fields.Str()
    bairro = fields.Str()
    referencia = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()