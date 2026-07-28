from pylons import c, request, g
from pylons.i18n import _
from pylons.controllers.util import abort
from r2.lib import utils, captcha
from r2.lib.filters import unkeep_space, websafe, _force_utf8, _force_ascii
from r2.lib.db.operators import asc, desc
from r2.config import cache
from r2.lib.template_helpers import add_sr
from r2.lib.jsonresponse import json_respond
from r2.models import *
from r2.controllers.errors import errors, UserRequiredException
from copy import copy
from datetime import datetime, timedelta
import re
default_param = None
def __init__(self, param=None, default=None, post=True, get=True, url=True):...
if param:
self.param = param
self.param = self.default_param
self.default = default
self.post, self.get, self.url = post, get, url
def __call__(self, url):...
a = []
if self.param:
for p in utils.tup(self.param):
return self.run(*a)
if self.post and request.post.get(p):
val = request.post[p]
if self.get and request.get.get(p):
a.append(val)
val = request.get[p]
if self.url and url.get(p):
val = url[p]
val = self.default
