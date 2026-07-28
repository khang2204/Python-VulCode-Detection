def test_imports(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('imports.py', expect)
