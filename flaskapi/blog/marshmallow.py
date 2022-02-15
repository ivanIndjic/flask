from marshmallow import fields, validates
from ..application import ma
from .blog import Blog
from ..post.marshmallow import PostSchema

from typing import List

class BlogSchema(ma.SQLAlchemyAutoSchema):
    title = fields.Str(required=True)
    posts = fields.List(fields.Nested(PostSchema))
    class Meta:
        fields = ['title', 'posts', 'id']
        exclude = ['id']
