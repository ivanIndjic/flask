from ..application import ma
from .blog import Blog


class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
        exclude = ['id']
