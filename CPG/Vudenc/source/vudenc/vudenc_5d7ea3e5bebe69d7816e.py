def test_new_connection_with_client_auth(self):...
mock_api = mock.Mock()
mock_api.nsxlib_config = mock.Mock()
mock_api.nsxlib_config.retries = 100
mock_api.nsxlib_config.insecure = True
mock_api.nsxlib_config.ca_file = None
mock_api.nsxlib_config.http_timeout = 99
mock_api.nsxlib_config.conn_idle_timeout = 39
cert_provider_inst = client_cert.ClientCertProvider('/etc/cert.pem')
mock_api.nsxlib_config.client_cert_provider = cert_provider_inst
provider = cluster.NSXRequestsHTTPProvider()
session = provider.new_connection(mock_api, cluster.Provider('9.8.7.6',
    'https://9.8.7.6', None, None, None))
self.assertIsNone(session.auth)
self.assertFalse(session.verify)
self.assertEqual(cert_provider_inst, session.cert_provider)
self.assertEqual(99, session.timeout)
