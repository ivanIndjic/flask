from ..application import ma
from .models import Post


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ['id', 'created_time', 'modified_time']
