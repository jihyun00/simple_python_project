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
    key = db.Column(db.String, nullable=False, default=random_string(20))

    def __repr__(self):
        return "<User(name='%s')>" % self.name


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())
    username = db.Column(db.String, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Tag(tag='%s', username='%s')>" % (self.tag, self.username)