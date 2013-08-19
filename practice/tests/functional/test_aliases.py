from practice.tests import *

class TestCreateAliasController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='create_alias', action='index'))
        # Test response...
