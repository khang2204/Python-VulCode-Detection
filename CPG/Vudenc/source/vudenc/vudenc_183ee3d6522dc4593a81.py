def test_client_update(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.update('unique-id', jsonutils.dumps({'name': 'a-new-name'}))
assert_call('put', api, 'https://1.2.3.4/api/v1/ports/unique-id', data=
    jsonutils.dumps({'name': 'a-new-name'}))
