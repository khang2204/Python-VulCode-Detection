def test_secret_config_option(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'MEDIUM': 2}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('secret-config-option.py', expect)
