from flaskapi.application import db
from ..post.models import Post


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    posts = db.relationship('Post', backref='blog',
                            lazy='select')



