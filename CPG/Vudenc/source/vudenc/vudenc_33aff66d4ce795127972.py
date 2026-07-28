def test_requests_ssl_verify_disabled(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('requests-ssl-verify-disabled.py', expect)
