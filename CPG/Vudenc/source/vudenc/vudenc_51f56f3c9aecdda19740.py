def test_timeouts(self):...
api = self.mock_nsx_clustered_api(http_read_timeout=37, http_timeout=7)
api.get('logical-ports')
mock_call = api.recorded_calls.method_calls[0]
name, args, kwargs = mock_call
self.assertEqual(kwargs['timeout'], (7, 37))
