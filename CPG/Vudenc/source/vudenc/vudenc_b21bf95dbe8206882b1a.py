from __future__ import unicode_literals, print_function, division
import contextlib
import httplib
import uuid
from logging import getLogger
from markupsafe import Markup
from tornado.escape import xhtml_escape
from veil.frontend.template import template_utility
from veil.frontend.web.tornado import *
LOGGER = getLogger(__name__)
@contextlib.contextmanager...
request = get_current_http_request()
response = get_current_http_response()
if not hasattr(request, '_xsrf_token'):
token = get_cookie(name='_xsrf', request=request)
if 'GET' != request.method.upper():
request.is_new_xsrf_token = False
token = get_http_argument('_xsrf', optional=True) or request.headers.get(
    'X-XSRF', None)
request.arguments.pop('_xsrf', None)
if not token:
if not token:
yield
request.is_new_xsrf_token = True
request._xsrf_token = token
response.status_code = httplib.FORBIDDEN
expected_token = xsrf_token()
def set_xsrf_cookie_for_page(route_handler, data):...
token = uuid.uuid4().get_hex()
LOGGER.warn('XSRF token not found: request is %(request)s', {'request': str
    (request)})
if expected_token != token:
if get_current_http_request().is_new_xsrf_token:
LOGGER.debug('assigned XSRF token: %(token)s from %(method)s %(path)s', {
    'token': token, 'method': request.method, 'path': request.path})
LOGGER.warn(
    'XSRF token invalid: request is %(request)s, expected is %(expected_token)s, actual is %(token)s'
    , {'request': request, 'expected_token': expected_token, 'token': token})
if data and '<html' in data.lower():
return data
set_cookie(name='_xsrf', value=xsrf_token())
