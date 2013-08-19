""" User model """
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from practice.model.meta import Base

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True)
    email = Column(String(100))
    password = Column(String(100))

    def __init__(self, email='', password=''):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('%s','%s')>" % (self.email, self.password)
