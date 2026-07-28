import logging
import traceback
from fuel_health.common.utils.data_utils import rand_name
from fuel_health import nmanager
LOG = logging.getLogger(__name__)
"""Test suit verifies:
     - keypairs creation
     - security groups creation
     - Network creation
     - Instance creation
     - Floating ip creation
     - Instance connectivity by floating IP
    """
@classmethod...
super(TestNovaNetwork, cls).setUpClass()
if cls.manager.clients_initialized:
cls.tenant_id = cls.manager._get_identity_client(cls.config.identity.
    admin_username, cls.config.identity.admin_password, cls.config.identity
    .admin_tenant_name).tenant_id
def setUp(self):...
cls.keypairs = {}
super(TestNovaNetwork, self).setUp()
cls.security_groups = {}
self.check_clients_state()
cls.network = []
if not self.config.compute.compute_nodes:
cls.servers = []
self.skipTest('There are no compute nodes')
def tearDown(self):...
cls.floating_ips = []
super(TestNovaNetwork, self).tearDown()
if self.manager.clients_initialized:
if self.servers:
def test_001_create_keypairs(self):...
for server in self.servers:
"""docstring"""
self._delete_server(server)
LOG.debug(traceback.format_exc())
self.keypairs[self.tenant_id] = self.verify(30, self._create_keypair, 1,
    'Keypair can not be created.', 'keypair creation', self.compute_client)
self.servers.remove(server)
LOG.debug('Server was already deleted.')
def test_002_create_security_groups(self):...
"""docstring"""
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
def test_003_check_networks(self):...
"""docstring"""
seen_nets = self.verify(50, self._list_networks, 1,
    'List of networks is not available.', 'listing networks')
seen_labels, seen_ids = zip(*((n.label, n.id) for n in seen_nets))
for mynet in self.network:
self.verify_response_body(seen_labels, mynet.label,
    'Network can not be created.properly', failed_step=2)
def test_004_create_servers(self):...
self.verify_response_body(seen_ids, mynet.id,
    'Network can not be created. properly ', failed_step=3)
"""docstring"""
self.check_image_exists()
if not self.security_groups:
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
name = rand_name('ost1_test-server-smoke-')
security_groups = [self.security_groups[self.tenant_id].name]
server = self.verify(200, self._create_server, 2,
    'Creating instance using the new security group has failed.',
    'image creation', self.compute_client, name, security_groups)
self.verify(30, self._delete_server, 3, 'Server can not be deleted.',
    'server deletion', server)
def test_008_check_public_instance_connectivity_from_instance(self):...
"""docstring"""
self.check_image_exists()
if not self.security_groups:
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
name = rand_name('ost1_test-server-smoke-')
security_groups = [self.security_groups[self.tenant_id].name]
server = self.verify(250, self._create_server, 2,
    'Server can not be created.', 'server creation', self.compute_client,
    name, security_groups)
floating_ip = self.verify(20, self._create_floating_ip, 3,
    'Floating IP can not be created.', 'floating IP creation')
self.verify(20, self._assign_floating_ip_to_instance, 4,
    'Floating IP can not be assigned.', 'floating IP assignment', self.
    compute_client, server, floating_ip)
self.floating_ips.append(floating_ip)
ip_address = floating_ip.ip
LOG.info('is address is  {0}'.format(ip_address))
LOG.debug(ip_address)
self.verify(600, self._check_vm_connectivity, 5,
    'VM connectivity doesn`t function properly.',
    'VM connectivity checking', ip_address, 30, (9, 60))
self.verify(600, self._check_connectivity_from_vm, 6,
    'Connectivity to 8.8.8.8 from the VM doesn`t function properly.',
    'public connectivity checking from VM', ip_address, 30, (9, 60))
self.verify(20, self.compute_client.servers.remove_floating_ip, 7,
    'Floating IP cannot be removed.', 'removing floating IP', server,
    floating_ip)
self.verify(20, self.compute_client.floating_ips.delete, 8,
    'Floating IP cannot be deleted.', 'floating IP deletion', floating_ip)
if self.floating_ips:
self.floating_ips.remove(floating_ip)
self.verify(30, self._delete_server, 9, 'Server can not be deleted. ',
    'server deletion', server)
def test_006_check_internet_connectivity_instance_without_floatingIP(self):...
"""docstring"""
self.check_image_exists()
if not self.security_groups:
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
name = rand_name('ost1_test-server-smoke-')
security_groups = [self.security_groups[self.tenant_id].name]
server = self.verify(250, self._create_server, 2,
    'Server can not be created.', 'server creation', self.compute_client,
    name, security_groups)
for addr in server.addresses:
LOG.debug(traceback.format_exc())
self.verify(600, self._check_connectivity_from_vm, 3,
    'Connectivity to 8.8.8.8 from the VM doesn`t function properly.',
    'public connectivity checking from VM', instance_ip, 30, (9, 30), compute)
if addr.startswith('novanetwork'):
if not self.config.compute.use_vcenter:
self.fail(
    'Step 3 failed: cannot get instance details. Please refer to OpenStack logs for more details.'
    )
self.verify(30, self._delete_server, 4, 'Server can not be deleted. ',
    'server deletion', server)
instance_ip = server.addresses[addr][0]['addr']
compute = getattr(server, 'OS-EXT-SRV-ATTR:host')
compute = None
def test_009_create_server_with_file(self):...
"""docstring"""
self.check_image_exists()
if not self.security_groups:
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
name = rand_name('ost1_test-server-smoke-file_inj-')
security_groups = [self.security_groups[self.tenant_id].name]
data_file = {'/home/cirros/server.txt': self._load_file('server.txt')}
server = self.verify(300, self._create_server, 2,
    'Creating instance using the new security group has failed.',
    'instance creation', self.compute_client, name, security_groups,
    data_file=data_file)
floating_ip = self.verify(20, self._create_floating_ip, 3,
    'Floating IP can not be created.', 'floating IP creation')
self.verify(20, self._assign_floating_ip_to_instance, 3,
    'Floating IP can not be assigned.', 'floating IP assignment', self.
    compute_client, server, floating_ip)
self.floating_ips.append(floating_ip)
ip_address = floating_ip.ip
self.verify(600, self._run_command_from_vm, 4,
    'Can not find injected file on instance.',
    'check if injected file exists', ip_address, 30, (9, 60),
    '[ -f /home/cirros/server.txt ] && echo "True" || echo "False"')
self.verify(20, self.compute_client.servers.remove_floating_ip, 5,
    'Floating IP cannot be removed.', 'removing floating IP', server,
    floating_ip)
self.verify(20, self.compute_client.floating_ips.delete, 5,
    'Floating IP cannot be deleted.', 'floating IP deletion', floating_ip)
if self.floating_ips:
self.floating_ips.remove(floating_ip)
self.verify(30, self._delete_server, 6, 'Server can not be deleted. ',
    'server deletion', server)
