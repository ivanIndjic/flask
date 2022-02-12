from ..application import db
from ..application import ma


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(90))
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author', lazy='select')

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'Author: [{self.full_name}, {self.email}, {self.posts}]'

