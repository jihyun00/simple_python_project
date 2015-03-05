import string
import random

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import functions
from sqlalchemy.ext.declarative import declarative_base
from db import db

engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)


def random_string(size=40, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    key = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name
        self.reset_key()

    def reset_key(self):
        self.key = random_string(20)
        return self.key


class Tag(db.Model):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=functions.now())

    def __init__(self, tag):
        self.tag = tag
        self.created_at()