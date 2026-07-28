def read_xsrf_token(self, url):...
response = self.session.get(url)
for cookie in response.cookies:
if cookie.name == '_xsrf':
self.xsrf_token = cookie.value
