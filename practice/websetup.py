"""Setup the practice application"""
import logging

from practice import model
from practice.config.environment import load_environment
from practice.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup practice here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    from practice.model.meta import Base, Session

    log.info("Creating tables")

    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(bind=Session.bind)

    log.info("Successfully setup")
