def test_client_url_prefix(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='/cloud/api')
api.list()
assert_call('get', api, 'https://1.2.3.4/cloud/api')
api = self.new_mocked_client(client.RESTClient, url_prefix='/cloud/api')
api.url_list('v1/ports')
assert_call('get', api, 'https://1.2.3.4/cloud/api/v1/ports')
