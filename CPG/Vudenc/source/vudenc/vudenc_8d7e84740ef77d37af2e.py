def test_002_create_security_groups(self):...
"""docstring"""
self.security_groups[self.tenant_id] = self.verify(25, self.
    _create_security_group, 1, 'Security group can not be created.',
    'security group creation', self.compute_client)
