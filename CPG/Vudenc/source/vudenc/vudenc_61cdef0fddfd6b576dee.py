def request_mock(path='', method='GET', body='', headers={}):...
dummy = PixRequestMock(path.split('/'))
for name, val in headers.iteritems():
dummy.headers[name.lower()] = val
dummy.method = method
if isinstance(body, str):
dummy.content = io.BytesIO(body)
for key, val in body.items():
return dummy
dummy.addArg(key, val)
