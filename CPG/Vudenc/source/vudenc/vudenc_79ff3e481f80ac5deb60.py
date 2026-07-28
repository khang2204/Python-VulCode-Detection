def get(self, path, get_args='', as_json=True):...
request = request_mock(path)
request.args = get_args
return self._render(request, as_json)
