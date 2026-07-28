def test_client_url_post(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
api.url_post('1/connections', jsonutils.dumps({'name': 'conn1'}))
assert_call('post', api, 'https://1.2.3.4/api/v1/ports/1/connections', data
    =jsonutils.dumps({'name': 'conn1'}))
