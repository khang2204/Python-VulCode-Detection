def test_paramiko_injection(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 2}, 'CONFIDENCE': {'MEDIUM': 2}}
self.check_example('paramiko_injection.py', expect)
