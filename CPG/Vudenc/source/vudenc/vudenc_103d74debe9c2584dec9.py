@property...
"""docstring"""
token = None
if self.xsrf_token_header:
token = self.request.headers.get(self.xsrf_token_header)
if not token and self.xsrf_token_request_param:
param = self.request.get_all(self.xsrf_token_request_param)
return token
token = param[0] if param else None
