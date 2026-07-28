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
