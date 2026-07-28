def test_yaml(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('yaml_load.py', expect)
