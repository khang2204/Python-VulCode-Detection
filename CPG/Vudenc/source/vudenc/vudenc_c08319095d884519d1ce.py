"""Tools to help run tests against the Django app."""
import const
import utils
import scrape
import testutils.base
"""A base class for tests for the Django app."""
_USER_ID = 'k'
def setUp(self):...
super(ViewTestsBase, self).setUp()
self._xsrf_tool = utils.XsrfTool()
def login(self, is_admin=False):...
"""docstring"""
self.testbed.setup_env(user_email='kay@mib.gov', user_id=ViewTestsBase.
    _USER_ID, user_is_admin='1' if is_admin else '0', overwrite=True)
def xsrf_token(self, action_id):...
return self._xsrf_tool.generate_token(ViewTestsBase._USER_ID, action_id)
