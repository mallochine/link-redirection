"""The application's model objects"""
from practice.model.meta import Session, Base

from practice.model.user import User
from practice.model.alias import Alias

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
