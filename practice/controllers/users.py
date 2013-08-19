import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from practice.lib.base import BaseController, render

log = logging.getLogger(__name__)

# import relevant models
from practice.model.meta import Base, Session
from practice import model
from practice.model.user import User

class UsersController(BaseController):

    def register(self):

        email = request.params['email']
        password = request.params['password']

        new_user = User();

        new_user.email = email
        new_user.password = password

        Session.add( new_user )
        Session.commit()

        return_text = 'Your email is: %s<br />\n' % email
        return_text += 'Your password is: %s' % password

        return return_text
