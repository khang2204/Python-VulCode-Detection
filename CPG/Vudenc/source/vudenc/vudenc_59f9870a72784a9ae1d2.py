import abc
import logging
import urlparse
import datetime
import random
import yaml
import flask
from flask import request, session
from flask import abort, jsonify, redirect
from werkzeug.security import safe_str_cmp
from authomatic import Authomatic
from authomatic.providers import oauth2
from authomatic.adapters import WerkzeugAdapter
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from confidant.lib import cryptolib
from confidant.utils.misc import dict_deep_update
from confidant.app import app
from confidant.authnz import errors
def init_user_auth_class(*args, **kwargs):...
if not app.config['USE_AUTH']:
module = NullUserAuthenticator
module_name = app.config['USER_AUTH_MODULE'].lower()
logging.info('Initializing {} user authenticator'.format(module.auth_type))
if module_name == 'google':
return module(*args, **kwargs)
module = GoogleOauthAuthenticator
if module_name == 'saml':
module = SamlAuthenticator
if module_name == 'null':
module = NullUserAuthenticator
