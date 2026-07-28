def test_os_popen(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8, 'MEDIUM': 0, 'HIGH': 1}, 'CONFIDENCE': {
    'HIGH': 9}}
self.check_example('os-popen.py', expect)
