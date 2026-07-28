"""
XSRF is Cross-Site Request Forgery, where an attacker has a user follow a link that triggers an 
action on a site which the user did not intentionally want to perform (i.e. vote in 
a certain way). To prevent this, some actions are only possible if authorized via HTTP or if a
modtoken - a shared SHA1 hash - is included.  
"""
import random
import hashlib
from urlparse import urlparse
from decorator import decorator
from pylons import session, request, config
from pylons.controllers.util import abort
from pylons.i18n import _
def RequireInternalRequest(methods=['POST', 'GET', 'PUT', 'DELETE']):...
"""docstring"""
def _decorate(f, *a, **kw):...
def check():...
if not request.method in methods:
return True
if not request.environ.get('AUTH_TYPE') == 'cookie':
return True
if config.get('skip_authentication'):
return True
if request.environ.get('HTTP_REFERER'):
ref_url = urlparse(request.environ.get('HTTP_REFERER'))
if request.method == 'GET' and has_token():
ref_host = ref_url.hostname
return True
return False
if ref_url.port:
ref_host += ':' + str(ref_url.port)
if ref_host.endswith(request.environ['adhocracy.domain']):
if request.method != 'GET':
return True
