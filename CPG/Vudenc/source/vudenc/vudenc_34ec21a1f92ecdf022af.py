def test_popen_wrappers(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('popen_wrappers.py', expect)
