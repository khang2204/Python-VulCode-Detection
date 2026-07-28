def test_client_url_list(self):...
api = self.new_mocked_client(client.RESTClient, url_prefix='api/v1/ports')
json_headers = {'Content-Type': 'application/json'}
api.url_list('/connections', json_headers)
assert_call('get', api, 'https://1.2.3.4/api/v1/ports/connections', headers
    =_headers(**json_headers))
