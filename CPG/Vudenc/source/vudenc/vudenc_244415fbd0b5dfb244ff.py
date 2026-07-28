def test_os_spawn(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8}, 'CONFIDENCE': {'MEDIUM': 8}}
self.check_example('os-spawn.py', expect)
