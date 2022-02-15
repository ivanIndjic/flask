from flaskapi.application import db
from ..post.models import Post


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    posts = db.relationship('Post', backref='blog_id',
                            lazy='select')

    def __init__(self, title: str, posts: [Post] = []):
        self.title = title
        self.posts = posts


