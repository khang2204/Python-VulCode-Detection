import time
import mox
import paramiko
from cinder import context
from cinder import exception
from cinder.openstack.common import log as logging
from cinder.openstack.common import processutils
from cinder import test
from cinder.volume import configuration as conf
from cinder.volume.drivers import eqlx
LOG = logging.getLogger(__name__)
def setUp(self):...
super(DellEQLSanISCSIDriverTestCase, self).setUp()
self.configuration = mox.MockObject(conf.Configuration)
self.configuration.append_config_values(mox.IgnoreArg())
self.configuration.san_is_local = False
self.configuration.san_ip = '10.0.0.1'
self.configuration.san_login = 'foo'
self.configuration.san_password = 'bar'
self.configuration.san_ssh_port = 16022
self.configuration.san_thin_provision = True
self.configuration.eqlx_pool = 'non-default'
self.configuration.eqlx_use_chap = True
self.configuration.eqlx_group_name = 'group-0'
self.configuration.eqlx_cli_timeout = 30
self.configuration.eqlx_cli_max_retries = 5
self.configuration.eqlx_chap_login = 'admin'
self.configuration.eqlx_chap_password = 'password'
self.configuration.volume_name_template = 'volume_%s'
self._context = context.get_admin_context()
self.driver = eqlx.DellEQLSanISCSIDriver(configuration=self.configuration)
self.volume_name = 'fakevolume'
self.volid = 'fakeid'
self.connector = {'ip': '10.0.0.2', 'initiator':
    'iqn.1993-08.org.debian:01:222', 'host': 'fakehost'}
self.fake_iqn = 'iqn.2003-10.com.equallogic:group01:25366:fakev'
self.driver._group_ip = '10.0.1.6'
self.properties = {'target_discoverd': True, 'target_portal': '%s:3260' %
    self.driver._group_ip, 'target_iqn': self.fake_iqn, 'volume_id': 1}
self._model_update = {'provider_location': '%s:3260,1 %s 0' % (self.driver.
    _group_ip, self.fake_iqn), 'provider_auth': 'CHAP %s %s' % (self.
    configuration.eqlx_chap_login, self.configuration.eqlx_chap_password)}
def _fake_get_iscsi_properties(self, volume):...
return self.properties
