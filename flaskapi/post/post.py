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


@post.route('/delete/<int:id>', methods=['DELETE'])
def delete_post(id: int):
    post = Post.query.filter_by(id=id).first()
    if post:
        db.session.delete(post)
        db.session.commit()
        return make_response('Resource deleted successfully', 200)
    return make_response('Resource not found', 404)


@post.route('/update/<int:id>', methods=['PUT'])
def update_post(id: int):
    request_post = request.get_json(force=True)
    post_updated = Post(**request_post)
    old_post = Post.query.get(id)
    if old_post:
        old_post.name = post_updated.name
        old_post.created_time = post_updated.created_time
        old_post.modified_time = post_updated.modified_time
        old_post.author = post_updated.author
        old_post.blog = post_updated.blog
        db.session.commit()
        post_marshmallow = PostSchema()
        return make_response(jsonify(fields=post_marshmallow.dump(old_post)), 200)
    return make_response('Resource not found', 404)