def generate_xsrf_token(self, xsrf_token_data=None):...
"""docstring"""
return XSRFToken.generate([api.get_current_identity().to_bytes()],
    xsrf_token_data)
