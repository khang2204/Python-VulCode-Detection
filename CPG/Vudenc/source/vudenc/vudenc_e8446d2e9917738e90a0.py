def test_binding(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'MEDIUM': 1}}
self.check_example('binding.py', expect)
