def testXsrfRemoteRefresh(self):...
self.expected_requests([(
    'http://localhost/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'expiration_sec': 100,
    'xsrf_token': 'token'}), ('http://localhost/a', {'data': {'foo': 'bar'},
    'headers': {'X-XSRF-Token': 'token'}}, 'bar', None), (
    'http://localhost/auth/api/v1/accounts/self/xsrf_token', {'data': {},
    'headers': {'X-XSRF-Token-Request': '1'}}, {'expiration_sec': 100,
    'xsrf_token': 'token2'}), ('http://localhost/a', {'data': {'foo': 'bar'
    }, 'headers': {'X-XSRF-Token': 'token2'}}, 'foo', None)])
now = xsrf_client._utcnow()
remote = xsrf_client.XsrfRemote('http://localhost/')
remote.url_read('/a', data={'foo': 'bar'})
self.mock(xsrf_client, '_utcnow', lambda : now + datetime.timedelta(seconds=91)
    )
remote.url_read('/a', data={'foo': 'bar'})
