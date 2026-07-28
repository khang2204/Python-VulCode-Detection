def check_xsrf_cookie(self):...
"""docstring"""
token = self.request.headers.get('X-XSRF-TOKEN')
if not token:
token = self.get_argument('xsrf-token', default=None)
if not token:
if self.xsrf_token != token:
