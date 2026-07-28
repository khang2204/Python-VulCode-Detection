"""Integration with webapp2."""
import functools
import json
import logging
import urllib
import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import users
from components import utils
from . import api
from . import config
from . import delegation
from . import host_token
from . import ipaddr
from . import model
from . import openid
from . import tokens
__all__ = ['ApiHandler', 'AuthenticatingHandler',
    'gae_cookie_authentication', 'get_authenticated_routes',
    'oauth_authentication', 'openid_cookie_authentication',
    'require_xsrf_token_request', 'service_to_service_authentication']
def require_xsrf_token_request(f):...
"""docstring"""
@functools.wraps(f)...
if not self.request.headers.get('X-XSRF-Token-Request'):
return f(self, *args, **kwargs)
