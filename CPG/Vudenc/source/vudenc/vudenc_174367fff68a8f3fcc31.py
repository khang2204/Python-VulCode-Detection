def test_ciphers(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 13}, 'CONFIDENCE': {'HIGH': 13}}
self.check_example('ciphers.py', expect)
