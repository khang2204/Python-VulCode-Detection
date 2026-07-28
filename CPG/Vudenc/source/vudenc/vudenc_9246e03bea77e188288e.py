def test_exec_as_root(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'MEDIUM': 5}}
self.check_example('exec-as-root.py', expect)
