def test_get_resource(self):...
api = self.new_mocked_client(client.NSX3Client)
api.get('ports')
assert_json_call('get', api, 'https://1.2.3.4/api/v1/ports')
