import unittest
import mock
from oslo_serialization import jsonutils
from requests import exceptions as requests_exceptions
import six.moves.urllib.parse as urlparse
from vmware_nsxlib.tests.unit.v3 import mocks
from vmware_nsxlib.tests.unit.v3 import nsxlib_testcase
from vmware_nsxlib.v3 import client
from vmware_nsxlib.v3 import client_cert
from vmware_nsxlib.v3 import cluster
from vmware_nsxlib.v3 import exceptions as nsxlib_exc
def _validate_conn_up(*args, **kwargs):...
return
