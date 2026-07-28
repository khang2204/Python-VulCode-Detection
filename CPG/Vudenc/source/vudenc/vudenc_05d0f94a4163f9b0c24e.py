def test_mktemp(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 4}, 'CONFIDENCE': {'HIGH': 4}}
self.check_example('mktemp.py', expect)
