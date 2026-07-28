def test_client_list(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.list()
assert_call('get', api, 'https://1.2.3.4/api/v1/ports')
