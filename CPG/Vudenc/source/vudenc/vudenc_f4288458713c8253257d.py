from __future__ import absolute_import
from mock import MagicMock, patch
from six.moves.urllib_parse import quote_plus
from flask import url_for, session
from invenio.testsuite import make_test_suite, run_test_suite
from invenio.ext.sqlalchemy import db
from .helpers import OAuth2ClientTestCase
def setUp(self):...
params = lambda x: dict(request_token_params={'scope': ''}, base_url=
    'https://foo.bar/', request_token_url=None, access_token_url=
    'https://foo.bar/oauth/access_token', authorize_url=
    'https://foo.bar/oauth/authorize', consumer_key=x, consumer_secret=
    'testsecret')
self.app.config['OAUTHCLIENT_REMOTE_APPS'] = dict(test=dict(
    authorized_handler=self.handler, params=params('testid'), title=
    'MyLinkedTestAccount'), test_invalid=dict(authorized_handler=self.
    handler_invalid, params=params('test_invalidid'), title='Test Invalid'),
    full=dict(params=params('fullid'), title='Full'))
self.handled_resp = None
self.handled_remote = None
self.handled_args = None
self.handled_kwargs = None
from invenio.modules.oauthclient.models import RemoteToken, RemoteAccount
RemoteToken.query.delete()
RemoteAccount.query.delete()
db.session.commit()
def tearDown(self):...
self.handled_resp = None
self.handled_remote = None
self.handled_args = None
self.handled_kwargs = None
from invenio.modules.oauthclient.models import RemoteToken, RemoteAccount
RemoteToken.query.delete()
RemoteAccount.query.delete()
db.session.commit()
def handler(self, resp, remote, *args, **kwargs):...
self.handled_resp = resp
self.handled_remote = remote
self.handled_args = args
self.handled_kwargs = kwargs
return 'TEST'
