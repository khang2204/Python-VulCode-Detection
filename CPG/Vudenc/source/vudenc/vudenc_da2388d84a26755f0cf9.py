def test_client_create(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.create(body=jsonutils.dumps({'resource-name': 'port1'}))
assert_call('post', api, 'https://1.2.3.4/api/v1/ports', data=jsonutils.
    dumps({'resource-name': 'port1'}))
