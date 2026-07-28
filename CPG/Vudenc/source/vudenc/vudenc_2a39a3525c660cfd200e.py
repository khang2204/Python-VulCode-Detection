def test_wildcard_injection(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 4, 'MEDIUM': 0, 'LOW': 10}, 'CONFIDENCE': {
    'MEDIUM': 5, 'HIGH': 9}}
self.check_example('wildcard-injection.py', expect)
