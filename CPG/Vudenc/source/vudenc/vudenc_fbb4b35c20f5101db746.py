def test_asserts(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('assert.py', expect)
