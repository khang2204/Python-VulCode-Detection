def test_imports_from(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('imports-from.py', expect)
