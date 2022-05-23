from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ITVDN_1.src.models import Actor, Film


class FilmsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True

class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        load_instance = True


