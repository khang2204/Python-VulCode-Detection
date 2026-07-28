def test_ssl_insecure_version(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'MEDIUM': 10, 'HIGH': 7}, 'CONFIDENCE': {
    'LOW': 0, 'MEDIUM': 11, 'HIGH': 7}}
self.check_example('ssl-insecure-version.py', expect)
