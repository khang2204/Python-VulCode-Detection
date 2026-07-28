def test_subprocess_shell(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 3, 'MEDIUM': 1, 'LOW': 14}, 'CONFIDENCE': {
    'HIGH': 17, 'LOW': 1}}
self.check_example('subprocess_shell.py', expect)
