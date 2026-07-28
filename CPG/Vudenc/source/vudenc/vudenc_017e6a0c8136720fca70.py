def test_skip(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'HIGH': 5}}
self.check_example('skip.py', expect)
