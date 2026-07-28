def test_weak_cryptographic_key(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 8, 'HIGH': 6}, 'CONFIDENCE': {'HIGH': 14}}
self.check_example('weak_cryptographic_key_sizes.py', expect)
