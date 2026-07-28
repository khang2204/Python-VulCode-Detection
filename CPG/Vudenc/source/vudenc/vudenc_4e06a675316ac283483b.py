import json
import functools
import zope.security.interfaces
from twisted.internet import defer
from twisted.python import log, failure
from twisted.web import resource
from twisted.web.server import NOT_DONE_YET
from zope.component import queryAdapter, getUtility
from opennode.oms.config import get_config
from opennode.oms.endpoint.httprest.base import IHttpRestView, IHttpRestSubViewFactory
from opennode.oms.model.traversal import traverse_path
from opennode.oms.security.checker import proxy_factory
from opennode.oms.security.interaction import new_interaction
from opennode.oms.util import blocking_yield
from opennode.oms.zodb import db
def __init__(self, body=None, *args, **kwargs):...
super(HttpStatus, self).__init__(*args, **kwargs)
self.body = body
@property...
@property...
headers = {}
status_code = 404
status_description = 'Not Found'
status_code = 501
status_description = 'Not Implemented'
def __init__(self, url, *args, **kwargs):...
super(AbstractRedirect, self).__init__(*args, **kwargs)
self.url = url
@property...
return {'Location': self.url}
