import copy
from oslo_log import log
from oslo_serialization import jsonutils
import requests
from vmware_nsxlib.tests.unit.v3 import mocks
from vmware_nsxlib.tests.unit.v3 import nsxlib_testcase
from vmware_nsxlib.v3 import client
from vmware_nsxlib.v3 import exceptions as nsxlib_exc
LOG = log.getLogger(__name__)
CLIENT_PKG = 'vmware_nsxlib.v3.client'
DFT_ACCEPT_HEADERS = {'Accept': '*/*'}
def _headers(**kwargs):...
headers = copy.copy(DFT_ACCEPT_HEADERS)
headers.update(kwargs)
return headers
