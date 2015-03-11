from .db import db


class BaseMixin(object):

    id = db.Column(db.Integer, primary_key=True)

    __repr_attr__ = 'id',

    def __repr__(self):
        represents = []
        for attr in self.__repr_attr__:
            represents.append('{}={}'.format(attr, getattr(self, attr)))
        return '{0.__class__.__name__}({1}) @ {2}'.format(
            self, ', '.join(represents), hex(id(self)))