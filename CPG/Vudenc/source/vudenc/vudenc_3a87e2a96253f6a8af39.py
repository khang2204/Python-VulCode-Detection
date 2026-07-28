def test_url(httpbin):...
native = {'origin': '127.0.0.1', 'args': {}}
source = httpbin.url + '/get'
result = load_source(source)
assert isinstance(result, collections.Mapping)
result.pop('headers')
result.pop('url')
assert result == native
