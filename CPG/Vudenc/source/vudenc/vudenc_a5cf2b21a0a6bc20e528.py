def test_os_exec(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8}, 'CONFIDENCE': {'MEDIUM': 8}}
self.check_example('os-exec.py', expect)
