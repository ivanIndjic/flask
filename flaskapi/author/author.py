from flask import Blueprint, render_template, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

from .marshmallow import AuthorSchema
from .forms import RegisterForm
from ..application import db
from .models import Author

author_app = Blueprint('author_app', __name__, url_prefix='/author')


@author_app.route('/register', methods=['GET', 'POST'])
def registration():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        hashed_password = generate_password_hash(reg_form.password.data)
        author = Author(
            password=hashed_password,
            full_name=reg_form.full_name.data,
            email=reg_form.email.data
        )
        db.session.add(author)
        db.session.commit()
        return 'Validated'
    return render_template('author/register.html', form=reg_form)


@author_app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    author = Author.query.filter_by(email=email).first()
    if author:
        if check_password_hash(author.password, password):
            return 'SUCCESS'
    return 'ERROR'


@author_app.route('/', methods=['GET'])
def get_all_authors():
    authors = AuthorSchema(many=True)
    a = Author.query.first()
    print(a.posts)
    return make_response(
        jsonify(json_list=authors.dump(Author.query.all())), 200)


@author_app.route('/create', methods=['POST'], )
def create_author():
    request_author = request.get_json(force=True)
    author = Author(**request_author)
    author.password = generate_password_hash(author.password)
    already_exists = Author.query.filter_by(email=author.email).first()
    if already_exists:
        return make_response('Already exists', 404)
    db.session.add(author)
    db.session.commit()
    author_marshmallow = AuthorSchema()

    return make_response(jsonify(
        json_list=author_marshmallow.dump(author)), 200)


@author_app.route('/delete/<int:id>', methods=['DELETE'])
def delete_author(id: int):
    author = Author.query.filter_by(id=id).first()
    if author:
        db.session.delete(author)
        db.session.commit()
        return make_response('Resource deleted successfully', 200)
    return make_response('Resource not found', 404)


@author_app.route('/update/<int:id>', methods=['PUT'])
def update_author(id: int):
    request_author = request.get_json(force=True)
    author_updated = Author(**request_author)
    author_updated.password = generate_password_hash(author_updated.password)
    old_author = Author.query.get(id)
    if old_author:
        old_author.full_name = author_updated.full_name
        old_author.email = author_updated.email
        old_author.password = author_updated.password
        db.session.commit()
        author_marshmallow = AuthorSchema()
        return make_response(jsonify(fields=author_marshmallow.dump(old_author)), 200)
    return make_response('Resource not found', 404)

