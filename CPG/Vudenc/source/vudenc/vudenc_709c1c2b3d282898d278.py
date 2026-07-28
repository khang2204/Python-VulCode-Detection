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
