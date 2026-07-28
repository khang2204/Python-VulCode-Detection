def test_cipher_modes(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('cipher-modes.py', expect)
