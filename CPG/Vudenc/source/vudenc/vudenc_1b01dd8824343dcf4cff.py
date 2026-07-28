def verify_xsrf_token(self):...
"""docstring"""
token = self.xsrf_token
if not token:
return XSRFToken.validate(token, [api.get_current_identity().to_bytes()])
