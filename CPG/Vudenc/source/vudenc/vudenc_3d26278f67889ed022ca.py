import copy
import unittest
import mock
from oslo_serialization import jsonutils
from oslo_utils import uuidutils
from requests import exceptions as requests_exceptions
from vmware_nsxlib import v3
from vmware_nsxlib.v3 import client as nsx_client
from vmware_nsxlib.v3 import client_cert
from vmware_nsxlib.v3 import cluster as nsx_cluster
from vmware_nsxlib.v3 import config
NSX_USER = 'admin'
NSX_PASSWORD = 'default'
NSX_MANAGER = '1.2.3.4'
NSX_INSECURE = False
NSX_CERT = '/opt/stack/certs/nsx.pem'
CLIENT_CERT = '/opt/stack/certs/client.pem'
NSX_HTTP_RETRIES = 10
NSX_HTTP_TIMEOUT = 10
NSX_HTTP_READ_TIMEOUT = 180
NSX_CONCURENT_CONN = 10
NSX_CONN_IDLE_TIME = 10
NSX_MAX_ATTEMPTS = 10
PLUGIN_SCOPE = 'plugin scope'
PLUGIN_TAG = 'plugin tag'
PLUGIN_VER = 'plugin ver'
DNS_NAMESERVERS = ['1.1.1.1']
DNS_DOMAIN = 'openstacklocal'
def _mock_nsxlib():...
def _return_id_key(*args, **kwargs):...
return {'id': uuidutils.generate_uuid()}
