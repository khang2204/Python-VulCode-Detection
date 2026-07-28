def test_validate_connection(self):...
self.skipTest('Revist')
mock_conn = mocks.MockRequestSessionApi()
mock_ep = mock.Mock()
mock_ep.provider.url = 'https://1.2.3.4'
provider = cluster.NSXRequestsHTTPProvider()
self.assertRaises(nsxlib_exc.ResourceNotFound, provider.validate_connection,
    mock.Mock(), mock_ep, mock_conn)
mock_conn.post('api/v1/transport-zones', data=jsonutils.dumps({'id':
    'dummy-tz'}), headers=client.JSONRESTClient._DEFAULT_HEADERS)
provider.validate_connection(mock.Mock(), mock_ep, mock_conn)
