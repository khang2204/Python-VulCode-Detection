def testXsrfRemoteGET(self):...
self.expected_requests([('http://localhost/a', {}, 'foo', None)])
remote = xsrf_client.XsrfRemote('http://localhost/')
self.assertEqual('foo', remote.url_read('/a'))
