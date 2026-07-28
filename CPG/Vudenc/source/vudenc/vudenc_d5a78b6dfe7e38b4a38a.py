def test_urlopen(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 14}, 'CONFIDENCE': {'HIGH': 14}}
self.check_example('urlopen.py', expect)
