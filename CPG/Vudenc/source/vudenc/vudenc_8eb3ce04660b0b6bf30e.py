def post(self, path, body='', headers=None):...
headers = headers or {'Content-Type': 'application/json'}
request = request_mock(path=path, method='POST', body=body, headers=headers)
return self._render(request)
