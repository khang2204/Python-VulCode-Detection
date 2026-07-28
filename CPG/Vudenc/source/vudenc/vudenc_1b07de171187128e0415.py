def test_imports_function(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('imports-function.py', expect)
