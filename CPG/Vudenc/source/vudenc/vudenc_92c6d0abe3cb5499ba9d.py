import fnmatch
import logging
from flask import abort, request, g
from flask import url_for
from functools import wraps
from confidant import keymanager
from confidant.app import app
from confidant.utils import stats
from confidant.authnz.errors import UserUnknownError, TokenVersionError, AuthenticationError, NotAuthorized
from confidant.authnz import userauth
PRIVILEGES = {'user': ['*'], 'service': ['get_service']}
user_mod = userauth.init_user_auth_class()
def get_logged_in_user():...
"""docstring"""
if hasattr(g, 'username'):
return g.username
if user_mod.is_authenticated():
return user_mod.current_email()
def user_is_user_type(user_type):...
if not app.config.get('USE_AUTH'):
return True
if user_type == g.user_type:
return True
return False
