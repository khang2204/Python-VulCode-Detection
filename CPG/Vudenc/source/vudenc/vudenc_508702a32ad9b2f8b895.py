def test_utils_shell(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'HIGH': 5}}
self.check_example('utils-shell.py', expect)
