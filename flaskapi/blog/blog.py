from flask import Blueprint, request

from .models import Blog
from ..application import db

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.get('/')
def init():
    return 'Blog Home'


@blog.post('/create')
def create():
    print(request)
    return str(request.json)
    # body = request.json
    # print(body)
    # new_blog = Blog(name=body['name'])
    # db.session.add(new_blog)
    # db.session.commit()
