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
