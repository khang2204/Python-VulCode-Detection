def test_client_url_get(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.url_get('connections/1')
assert_call('get', api, 'https://1.2.3.4/api/v1/ports/connections/1')
