from flask import Blueprint
from .models import Post

post = Blueprint('post', __name__, url_prefix='/post')


@post.get('/')
def init():
    return 'Post'