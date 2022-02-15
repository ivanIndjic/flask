from flask import Blueprint, request, jsonify, make_response
from flask_jwt import jwt_required
from flask_restful import reqparse
from marshmallow import ValidationError

from .models import Blog
from .marshmallow import BlogSchema
from ..application import db

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/', methods=['GET'])
def get_all_blogs():
    print(request.headers)
    blogs = BlogSchema(many=True)
    return make_response(jsonify(
        blogs=blogs.dump(Blog.query.all())), 200)


@blog.route('/create', methods=['POST'])
@jwt_required()
def create_blog():
    blog_schema = BlogSchema()
    new_blog = request.get_json(force=True)
    try:
        result = blog_schema.load(new_blog)
        print(result)
        new_blog = Blog(**new_blog)
        already_exists = Blog.query.filter_by(title=new_blog.title).first()
        if already_exists:
            return make_response('Already exists', 404)
        db.session.add(new_blog)
        db.session.commit()
        blog_marshmallow = BlogSchema()
        return make_response(jsonify(
            fields=blog_marshmallow.dump(new_blog)), 200)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400


@blog.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_blog(id: int):
    blog = Blog.query.filter_by(id=id).first()
    if blog:
        db.session.delete(blog)
        db.session.commit()
        return make_response('Resource deleted successfully', 200)
    return make_response('Resource not found', 404)


@blog.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_blog(id: int):

    request_blog = request.get_json(force=True)
    blog_schema = BlogSchema()
    try:
        result = blog_schema.load(request_blog)
        print(result)
        blog_updated = Blog(**request_blog)
        old_blog = Blog.query.get(id)
        if old_blog:
            old_blog.title = blog_updated.title
            old_blog.posts = blog_updated.posts
            db.session.commit()
            blog_marshmallow = BlogSchema()
            return make_response(jsonify(fields=blog_marshmallow.dump(old_blog)), 200)
    except ValidationError as err:
        # Return a nice message if validation fails
        return make_response(jsonify(err.messages), 400)
