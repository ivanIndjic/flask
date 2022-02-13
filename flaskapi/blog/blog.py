from flask import Blueprint, request, jsonify, make_response

from .models import Blog
from .marshmallow import BlogSchema
from ..application import db

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/', methods=['GET'])
def get_all_blogs():
    blogs = BlogSchema(many=True)
    return make_response(jsonify(
        blogs=blogs.dump(Blog.query.all())), 200)


@blog.route('/create', methods=['POST'])
def create_blog():
    new_blog = request.get_json(force=True)
    new_blog = Blog(**new_blog)
    already_exists = Blog.query.filter_by(title=new_blog.title).first()
    if already_exists:
        return make_response('Already exists', 404)
    db.session.add(new_blog)
    db.session.commit()
    blog_marshmallow = BlogSchema()
    return make_response(jsonify(
        fields=blog_marshmallow.dump(new_blog)), 200)


@blog.route('/delete/<int:id>', methods=['DELETE'])
def delete_blog(id: int):
    blog = Blog.query.filter_by(id=id).first()
    if blog:
        db.session.delete(blog)
        db.session.commit()
        return make_response('Resource deleted successfully', 200)
    return make_response('Resource not found', 404)


@blog.route('/update/<int:id>', methods=['PUT'])
def update_blog(id: int):
    request_blog = request.get_json(force=True)
    blog_updated = Blog(**request_blog)
    old_blog = Blog.query.get(id)
    if old_blog:
        old_blog.title = blog_updated.title
        old_blog.posts = blog_updated.posts
        db.session.commit()
        blog_marshmallow = BlogSchema()
        return make_response(jsonify(fields=blog_marshmallow.dump(old_blog)), 200)
    return make_response('Resource not found', 404)