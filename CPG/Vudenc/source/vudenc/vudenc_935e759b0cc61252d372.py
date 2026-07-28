def test_client_get(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.get('unique-id')
assert_call('get', api, 'https://1.2.3.4/api/v1/ports/unique-id')
