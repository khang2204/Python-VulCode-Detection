from functools import wraps
import os
import json
from base64 import b64encode
import time as time_module
from copy import copy
import logging
from six.moves.urllib.parse import urlencode
from flask import request, session, redirect, url_for, g
from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow, AccessTokenRefreshError
import httplib2
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
__all__ = ['OpenIDConnect', 'MemoryCredentials']
logger = logging.getLogger(__name__)
"""
    Non-persistent local credentials store.
    Use this if you only have one app server, and don't mind making everyone
    log in again after a restart.
    """
"""
    @see: https://developers.google.com/api-client-library/python/start/get_started
    @see: https://developers.google.com/api-client-library/python/samples/authorized_api_web_server_calendar.py
    """
def __init__(self, app=None, credentials_store=None, http=None, time=None,...
self.credentials_store = (credentials_store if credentials_store is not
    None else MemoryCredentials())
self.http = http if http is not None else httplib2.Http()
self.time = time if time is not None else time_module.time
self.urandom = urandom if urandom is not None else os.urandom
if app is not None:
self.init_app(app)
def init_app(self, app):...
"""docstring"""
self.app = app
app.config.setdefault('OIDC_SCOPES', ['openid', 'email'])
app.config.setdefault('OIDC_GOOGLE_APPS_DOMAIN', None)
app.config.setdefault('OIDC_ID_TOKEN_COOKIE_NAME', 'oidc_id_token')
app.config.setdefault('OIDC_ID_TOKEN_COOKIE_TTL', 7 * 86400)
app.config.setdefault('OIDC_ID_TOKEN_COOKIE_SECURE', True)
app.config.setdefault('OIDC_VALID_ISSUERS', ['accounts.google.com',
    'https://accounts.google.com'])
app.config.setdefault('OIDC_CLOCK_SKEW', 60)
app.config.setdefault('OIDC_REQUIRE_VERIFIED_EMAIL', True)
app.route('/oidc_callback')(self.oidc_callback)
app.before_request(self.before_request)
app.after_request(self.after_request)
self.flow = flow_from_clientsecrets(app.config['OIDC_CLIENT_SECRETS'],
    scope=app.config['OIDC_SCOPES'])
assert isinstance(self.flow, OAuth2WebServerFlow)
self.cookie_serializer = TimedJSONWebSignatureSerializer(app.config[
    'SECRET_KEY'])
self.credentials_store = app.config['OIDC_CREDENTIALS_STORE']
def get_cookie_id_token(self):...
id_token_cookie = request.cookies[self.app.config['OIDC_ID_TOKEN_COOKIE_NAME']]
logger.debug('Missing or invalid ID token cookie', exc_info=True)
def set_cookie_id_token(self, id_token):...
return self.cookie_serializer.loads(id_token_cookie)
return None
"""docstring"""
g.oidc_id_token = id_token
g.oidc_id_token_dirty = True
def after_request(self, response):...
"""docstring"""
if getattr(g, 'oidc_id_token_dirty', False):
signed_id_token = self.cookie_serializer.dumps(g.oidc_id_token)
return response
response.set_cookie(self.app.config['OIDC_ID_TOKEN_COOKIE_NAME'],
    signed_id_token, secure=self.app.config['OIDC_ID_TOKEN_COOKIE_SECURE'],
    httponly=True, max_age=self.app.config['OIDC_ID_TOKEN_COOKIE_TTL'])
