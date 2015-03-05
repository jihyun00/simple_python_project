import string
import random
from datetime import datetime
from .db import db


def random_string(size=40, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name
        self.reset_key()

    def reset_key(self):
        self.key = random_string(20)
        return self.key

    def __repr__(self):
        return "<User %r>" % self.name


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())

    def __init__(self, tag):
        self.tag = tag