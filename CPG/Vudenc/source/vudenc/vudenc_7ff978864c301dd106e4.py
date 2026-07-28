def test_delete_resource(self):...
api = self.new_mocked_client(client.NSX3Client)
api.delete('ports/11')
assert_json_call('delete', api, 'https://1.2.3.4/api/v1/ports/11')
