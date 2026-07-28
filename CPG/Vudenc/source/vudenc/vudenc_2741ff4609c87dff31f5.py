"""Handlers for customizing oauthclient endpoints."""
import six
from flask import current_app, flash, redirect, render_template, request, session, url_for
from flask.ext.login import current_user
from functools import partial, wraps
from werkzeug.utils import import_string
from invenio.base.globals import cfg
from .client import oauth, signup_handlers
from .errors import OAuthClientError, OAuthError, OAuthRejectedRequestError, OAuthResponseError
from .forms import EmailSignUpForm
from .models import RemoteAccount, RemoteToken
from .utils import oauth_authenticate, oauth_get_user, oauth_register
def token_session_key(remote_app):...
"""docstring"""
return '%s_%s' % (cfg['OAUTHCLIENT_SESSION_KEY_PREFIX'], remote_app)
