def test_crypto_md5(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 11}, 'CONFIDENCE': {'HIGH': 11}}
self.check_example('crypto-md5.py', expect)
