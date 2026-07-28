def test_httplib_https(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('httplib_https.py', expect)
