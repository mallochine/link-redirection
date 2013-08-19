""" User model """
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from practice.model.meta import Base

class Alias(Base):
    __tablename__ = "aliases"

    aliasid = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(100))

    def __init__(self, name='', url=''):
        self.name = name
        self.url = url

    def __repr__(self):
        return "<Alias('%s','%s')>" % (self.name, self.url)
