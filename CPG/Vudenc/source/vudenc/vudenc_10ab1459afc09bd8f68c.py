def test_create_resource(self):...
api = self.new_mocked_client(client.NSX3Client)
api.create('ports', {'resource-name': 'port1'})
assert_json_call('post', api, 'https://1.2.3.4/api/v1/ports', data=
    jsonutils.dumps({'resource-name': 'port1'}))
