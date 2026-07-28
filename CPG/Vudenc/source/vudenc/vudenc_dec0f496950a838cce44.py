def test_imports_aliases(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 4, 'MEDIUM': 5, 'HIGH': 0}, 'CONFIDENCE': {
    'HIGH': 9}}
self.check_example('imports-aliases.py', expect)
