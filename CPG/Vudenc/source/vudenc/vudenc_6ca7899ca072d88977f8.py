import requests
def _store_xsrf_token(self, response):...
xsrf_token = response.cookies.get('XSRF-TOKEN')
if xsrf_token:
self.xsrf_token = xsrf_token
def _set_xsrf_headers(self, kwargs):...
xsrf_header = {'X-XSRF-TOKEN': self.xsrf_token}
if 'headers' in kwargs:
kwargs['headers'].update(xsrf_header)
kwargs['headers'] = xsrf_header
return kwargs
