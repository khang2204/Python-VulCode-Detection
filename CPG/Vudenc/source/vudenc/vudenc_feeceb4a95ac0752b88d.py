def delete(self, path, body=''):...
request = request_mock(path=path, body=body, headers={'Content-Type': [
    'application/json']}, method='DELETE')
return self._render(request)
