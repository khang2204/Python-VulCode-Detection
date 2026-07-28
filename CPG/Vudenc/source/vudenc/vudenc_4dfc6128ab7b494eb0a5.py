def test_client_delete(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.delete('unique-id')
assert_call('delete', api, 'https://1.2.3.4/api/v1/ports/unique-id')
