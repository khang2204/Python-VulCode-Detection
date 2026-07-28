def put(self, path, body):...
request = request_mock(path=path, method='PUT', body=body, headers={
    'Content-Type': ['application/json']})
return self._render(request)
