def test_001_create_keypairs(self):...
"""docstring"""
self.keypairs[self.tenant_id] = self.verify(30, self._create_keypair, 1,
    'Keypair can not be created.', 'keypair creation', self.compute_client)
