def test_partial_path(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 11}, 'CONFIDENCE': {'HIGH': 11}}
self.check_example('partial_path_process.py', expect)
