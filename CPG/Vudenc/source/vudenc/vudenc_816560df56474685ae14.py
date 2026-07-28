def test_client_url_put(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.url_put('connections/1', jsonutils.dumps({'name': 'conn1'}))
assert_call('put', api, 'https://1.2.3.4/api/v1/ports/connections/1', data=
    jsonutils.dumps({'name': 'conn1'}))
