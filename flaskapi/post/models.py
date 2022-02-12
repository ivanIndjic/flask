from ..application import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))