import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from practice.lib.base import BaseController, render

log = logging.getLogger(__name__)

# Import relevant models
from practice.model.meta import Base, Session
from practice import model
from practice.model.alias import Alias

# Debugging tools
import pprint

class AliasesController(BaseController):

    def __before__(self):
        self.alias_q = Session.query(Alias)

    def create(self):

        name = request.params['name']
        url = request.params['url']

        new_alias = Alias();

        new_alias.name = name
        new_alias.url = url;

        Session.add( new_alias )
        Session.commit()

        return_text = 'Your alias\'s name is: %s<br>\n' % name
        return_text += 'The url is: %s<br>' % url

        c.body = return_text
        c.title = 'Alias creation'
        c.heading = 'Result'
        c.name = name
        c.url = url

        return render('/derived/aliases/creation_result.mako')

    def create_alias_form(self):

        c.title = "Create an Alias"
        c.heading = "Create an Alias"
        return render('/derived/aliases/create_alias_form.mako')

    def displayAll(self):

        c.aliases = self.alias_q.all()

        return render('/derived/aliases/all_aliases.mako')

    def answer(self, query):
        closest_match = (self.alias_q
                        .filter_by(name=query)
                        .order_by(Alias.aliasid.desc())
                        .first())
        if closest_match:
            return closest_match.url
        else:
            raise NoAnswer( query )

    def from_web_form(self):
        query = request.params['query']
        answer = self.answer( query )

        print "==========================="
        print "Answer:" + answer
        print "==========================="

        redirect( answer )

    def from_browser(self, query):
        answer = self.answer( query )

        print "==========================="
        print "Answer:" + answer
        print "==========================="

        redirect( answer )

    def alias_cli(self):
        c.title='Chestnut'
        c.heading='Chestnut'
        return render('/derived/aliases/alias_cli.mako')
