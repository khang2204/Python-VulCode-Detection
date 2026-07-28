def test_hardcoded_passwords(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'MEDIUM': 7}}
self.check_example('hardcoded-passwords.py', expect)
