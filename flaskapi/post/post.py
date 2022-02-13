from flask import Blueprint, make_response, jsonify, request

from ..application import db
from .models import Post
from .marshmallow import PostSchema

post = Blueprint('post', __name__, url_prefix='/post')


@post.route('/', methods=['GET'])
def get_all_posts():
    posts = PostSchema(many=True)
    return make_response(jsonify(
        posts=posts.dump(Post.query.all())), 200)


@post.route('/create', methods=['POST'])
def create_post():
    new_post = request.get_json(force=True)
    new_post = Post(**new_post)
    already_exists = Post.query.filter_by(
        name=new_post.name).first()
    if already_exists:
        return make_response('Already exists', 404)
    try:
        db.session.add(new_post)
        db.session.commit()
        post_marshmallow = PostSchema()

        return make_response(jsonify(
            fields=post_marshmallow.dump(new_post)), 200)
    except ValueError as e:
        raise ValueError(e)
