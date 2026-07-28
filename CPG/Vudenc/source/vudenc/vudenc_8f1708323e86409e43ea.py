def test_random_module(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 6}, 'CONFIDENCE': {'HIGH': 6}}
self.check_example('random_module.py', expect)
