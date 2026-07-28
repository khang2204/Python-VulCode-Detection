def test_004_create_servers(self):...
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
