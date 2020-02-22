from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

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