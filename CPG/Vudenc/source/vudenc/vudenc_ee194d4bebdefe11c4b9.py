def test_os_system(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('os_system.py', expect)
