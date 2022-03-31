from sqlalchemy.orm import validates

from ..application import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    created_time = db.Column(
        db.DateTime, server_default=db.func.now())
    modified_time = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    blog = db.Column(
        db.Integer, db.ForeignKey('blog.id', ondelete='NO ACTION'))
    author = db.Column(
        db.Integer, db.ForeignKey('author.id', ondelete='NO ACTION'))

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'Post: [{self.name}, {self.created_time}, {self.modified_time}]'
