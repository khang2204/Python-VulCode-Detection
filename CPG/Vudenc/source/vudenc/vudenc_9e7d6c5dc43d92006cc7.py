from __future__ import absolute_import
from functools import partial
import cherrypy
import cephfs
from . import ApiController, RESTController, UiApiController, BaseController, Endpoint, Task
from .. import logger
from ..security import Scope
from ..services.cephfs import CephFS
from ..services.cephx import CephX
from ..services.exception import serialize_dashboard_exception
from ..services.ganesha import Ganesha, GaneshaConf, NFSException
from ..services.rgw_client import RgwClient
def NfsTask(name, metadata, wait_for):...
def composed_decorator(func):...
return Task('nfs/{}'.format(name), metadata, wait_for, partial(
    serialize_dashboard_exception, include_http_status=True))(func)
