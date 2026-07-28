def test_client_headers(self):...
default_headers = {'Content-Type': 'application/golang'}
api = self.new_mocked_client(client.RESTClient, default_headers=
    default_headers, url_prefix='/v1/api')
api.list()
assert_call('get', api, 'https://1.2.3.4/v1/api', headers=_headers(**
    default_headers))
api = self.new_mocked_client(client.RESTClient, default_headers=
    default_headers, url_prefix='/v1/api')
method_headers = {'X-API-Key': 'strong-crypt'}
api.url_list('ports/33', headers=method_headers)
method_headers.update(default_headers)
assert_call('get', api, 'https://1.2.3.4/v1/api/ports/33', headers=_headers
    (**method_headers))
