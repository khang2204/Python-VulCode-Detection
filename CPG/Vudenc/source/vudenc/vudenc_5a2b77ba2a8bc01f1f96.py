def test_new_connection(self):...
mock_api = mock.Mock()
mock_api.nsxlib_config = mock.Mock()
mock_api.nsxlib_config.username = 'nsxuser'
mock_api.nsxlib_config.password = 'nsxpassword'
mock_api.nsxlib_config.retries = 100
mock_api.nsxlib_config.insecure = True
mock_api.nsxlib_config.ca_file = None
mock_api.nsxlib_config.http_timeout = 99
mock_api.nsxlib_config.conn_idle_timeout = 39
mock_api.nsxlib_config.client_cert_provider = None
provider = cluster.NSXRequestsHTTPProvider()
session = provider.new_connection(mock_api, cluster.Provider('9.8.7.6',
    'https://9.8.7.6', 'nsxuser', 'nsxpassword', None))
self.assertEqual(('nsxuser', 'nsxpassword'), session.auth)
self.assertFalse(session.verify)
self.assertIsNone(session.cert)
self.assertEqual(100, session.adapters['https://'].max_retries.total)
self.assertEqual(99, session.timeout)
