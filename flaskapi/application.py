from flask import Flask, current_app
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT


db = SQLAlchemy()
ma = Marshmallow()

from .author.security import authenticate, identity

def create_app(**config_overrides) -> Flask:

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    print(app.config['SECRET_KEY'])
    db.init_app(app)
    jwt = JWT(app, authenticate, identity)
    migrate = Migrate(app, db, compare_type=True)

    app.config.update(config_overrides)

    from flaskapi.blog.blog import blog
    from flaskapi.author.author import author_app
    from flaskapi.post.post import post
    app.register_blueprint(blog)
    app.register_blueprint(author_app)
    app.register_blueprint(post)
    ma.init_app(app)

    return app
