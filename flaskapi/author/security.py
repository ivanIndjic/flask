# Security
from .models import Author
from werkzeug.security import generate_password_hash, check_password_hash


def authenticate(username: str, password: str):
    author = Author.query.filter_by(email=username).first()
    if author:
        if check_password_hash(author.password, password):
            return author


def identity(payload):
    author_id = payload['identity']
    return Author.query.get(author_id) or None
