def test_update_resource(self):...
api = self.new_mocked_client(client.NSX3Client)
api.update('ports/1', {'name': 'a-new-name'})
assert_json_call('put', api, 'https://1.2.3.4/api/v1/ports/1', data=
    jsonutils.dumps({'name': 'a-new-name'}))
