def testXsrfRemoteCustom(self):...
self.expected_requests([('http://localhost/swarming/api/v1/bot/handshake',
    {'data': {'attributes': 'b'}, 'headers': {'X-XSRF-Token-Request': '1'}},
    {'expiration_sec': 100, 'ignored': True, 'xsrf_token': 'token'}), (
    'http://localhost/a', {'data': {'foo': 'bar'}, 'headers': {
    'X-XSRF-Token': 'token'}}, 'foo', None)])
remote = xsrf_client.XsrfRemote('http://localhost/',
    '/swarming/api/v1/bot/handshake')
remote.xsrf_request_params = {'attributes': 'b'}
self.assertEqual('foo', remote.url_read('/a', data={'foo': 'bar'}))
