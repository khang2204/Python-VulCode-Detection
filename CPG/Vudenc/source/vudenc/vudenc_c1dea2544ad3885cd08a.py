def test_ignore_skip(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('skip.py', expect, ignore_nosec=True)
