def _add_security_response_headers(self):...
"""docstring"""
self.response.headers['Strict-Transport-Security'
    ] = 'max-age=2592000; includeSubdomains'
self.response.headers['X-Content-Type-Options'] = 'nosniff'
self.response.headers['X-Frame-Options'] = 'deny'
