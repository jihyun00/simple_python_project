import string
import random

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()


def random_string(size=40, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    key = Column(String, nullable=False)

    def __init__(self, email):
        self.email = email
        self.reset_key()

    def reset_key(self):
        self.key = random_string(20)
        return self.key


# class Tag(Base):
#     __tablename__ = 'tag'
#
#     tag = Column(String)