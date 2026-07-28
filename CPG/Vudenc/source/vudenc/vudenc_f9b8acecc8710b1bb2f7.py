def testXsrfRemoteSimple(self):...
self.expected_requests([(
    'http://localhost/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'expiration_sec': 100,
    'xsrf_token': 'token'}), ('http://localhost/a', {'data': {'foo': 'bar'},
    'headers': {'X-XSRF-Token': 'token'}}, 'foo', None)])
remote = xsrf_client.XsrfRemote('http://localhost/')
self.assertEqual('foo', remote.url_read('/a', data={'foo': 'bar'}))
