import os
import time
import json
import base64
from hashlib import sha256
from werkzeug.exceptions import NotFound
from werkzeug.http import dump_cookie
from flask import session
from flask import Blueprint
from saml2.s_utils import deflate_and_base64_encode
from eduid_userdb.user import User
from eduid_userdb.data_samples import NEW_COMPLETED_SIGNUP_USER_EXAMPLE
from eduid_common.api.testing import EduidAPITestCase
from eduid_common.authn.cache import OutstandingQueriesCache
from eduid_common.authn.utils import get_location, no_authn_views
from eduid_common.authn.eduid_saml2 import get_authn_request
from eduid_common.authn.tests.responses import auth_response, logout_response, logout_request
from eduid_webapp.authn.app import authn_init_app
from eduid_common.api.app import eduid_init_app
import logging
logger = logging.getLogger(__name__)
HERE = os.path.abspath(os.path.dirname(__file__))
def update_config(self, config):...
"""docstring"""
saml_config = os.path.join(HERE, 'saml2_settings.py')
config.update({'SAML2_LOGIN_REDIRECT_URL': '/', 'SAML2_LOGOUT_REDIRECT_URL':
    '/logged-out', 'SAML2_SETTINGS_MODULE': saml_config,
    'TOKEN_LOGIN_SHARED_KEY': 'shared_secret',
    'TOKEN_LOGIN_SUCCESS_REDIRECT_URL': 'http://test.localhost/success',
    'TOKEN_LOGIN_FAILURE_REDIRECT_URL': 'http://test.localhost/failure'})
return config
