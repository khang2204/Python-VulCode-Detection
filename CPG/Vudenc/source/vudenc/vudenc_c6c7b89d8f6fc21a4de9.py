def test_os_startfile(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('os-startfile.py', expect)
