from flaskapi.application import ma
from flaskapi.author.models import Author


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        exclude = ['id', 'password']
