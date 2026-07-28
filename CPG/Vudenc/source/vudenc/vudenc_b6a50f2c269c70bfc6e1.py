def test_client_for(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/')
sub_api = api.new_client_for('switch/ports')
sub_api.get('11a2b')
assert_call('get', sub_api, 'https://1.2.3.4/api/v1/switch/ports/11a2b')
