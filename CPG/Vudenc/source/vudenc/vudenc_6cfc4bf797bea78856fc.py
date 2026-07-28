"""SchoolCMS-handler-init.

route.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .. import version as system_version
from ..db import SQL_Session, User, GroupList, Login_Session
from ..util import webassets_react
import functools
import os
from webassets import Environment, Bundle
import tornado.web
from tornado.escape import json_encode
from tornado.options import options
def initialize(self, is_api=True):...
self.is_api = is_api
self.assets = Environment(os.path.join(os.path.dirname(__file__),
    '../static'), '/static')
css_all = Bundle('css/bootstrap.min.css', 'css/material.min.css', Bundle(
    'css/schoolcms.css', 'css/dropdown.css', filters='cssmin'),
    'outdatedbrowser/outdatedbrowser.min.css', output='dict/plugin.min.css')
js_all = Bundle(Bundle('outdatedbrowser/outdatedbrowser.min.js',
    'react-0.13.2/react-with-addons.min.js', 'js/jquery-2.1.3.min.js',
    'js/bootstrap.min.js', 'js/react-bootstrap.min.js',
    'js/react-mini-router.min.js', 'js/marked.min.js', 'js/material.min.js',
    'js/isMobile.min.js', 'js/moment-with-locales.min.js', 'js/dropdown.js',
    filters='jsmin'), Bundle('schoolcms/init.jsx', 'schoolcms/mixin/*.jsx',
    'schoolcms/component/*.jsx', 'schoolcms/page/*.jsx', filters=('react',
    'jsmin')), output='dict/plugin.min.js')
self.assets.register('css_all', css_all)
self.assets.register('js_all', js_all)
def prepare(self):...
"""docstring"""
self.sql_session = SQL_Session()
def on_finish(self):...
"""docstring"""
self.sql_session.close()
def get_current_user(self):...
"""docstring"""
session_key = self.get_secure_cookie('session_key')
if not session_key:
return None
login_session = Login_Session.get_by_key(session_key, self.sql_session)
if not login_session:
return None
return User.by_key(login_session.userkey, self.sql_session).scalar()
