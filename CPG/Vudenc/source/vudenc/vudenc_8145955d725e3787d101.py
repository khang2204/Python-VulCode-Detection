def _store_xsrf_token(self, response):...
xsrf_token = response.cookies.get('XSRF-TOKEN')
if xsrf_token:
self.xsrf_token = xsrf_token
