import string
import random
from datetime import datetime

from .db import db
from .mixin import BaseMixin


def random_string(size=40, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class User(db.Model, BaseMixin):
    __tablename__ = 'users'

    __repr_attr__ = 'name',

    name = db.Column(db.String, nullable=False)
    key = db.Column(db.String, nullable=False, default=random_string(20))

    def __repr__(self):
        return "<User(name='%s')>" % self.name


class Tag(db.Model, BaseMixin):
    __tablename__ = 'tags'

    __repr_attr__ = 'name',

    tag = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow())
    username = db.Column(db.String, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Tag(tag='%s', username='%s')>" % (self.tag, self.username)