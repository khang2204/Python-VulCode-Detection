from saml2 import BINDING_HTTP_REDIRECT
from saml2.ident import decode
from saml2.client import Saml2Client
from saml2.response import LogoutResponse
from saml2.metadata import entity_descriptor
from werkzeug.exceptions import Forbidden
from flask import request, session, redirect, abort, make_response
from flask import current_app, Blueprint
from eduid_common.api.decorators import MarshalWith
from eduid_common.authn.utils import get_location
from eduid_common.authn.loa import get_loa
from eduid_common.authn.eduid_saml2 import get_authn_request, get_authn_response
from eduid_common.authn.eduid_saml2 import authenticate
from eduid_common.authn.cache import IdentityCache, StateCache
from eduid_webapp.authn.acs_registry import get_action, schedule_action
from eduid_webapp.authn.helpers import verify_auth_token
from eduid_webapp.authn.schemas import LogoutPayload, LogoutResponseSchema
authn_views = Blueprint('authn', __name__)
@authn_views.route('/login')...
"""docstring"""
return _authn('login-action')
