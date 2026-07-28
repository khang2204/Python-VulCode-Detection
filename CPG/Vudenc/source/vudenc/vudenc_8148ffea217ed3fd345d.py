def test_conf_providers_with_scheme(self):...
conf_managers = ['http://8.9.10.11:8080', 'https://9.10.11.12:4433']
api = self.new_mocked_cluster(conf_managers, _validate_conn_up)
self._assert_providers(api, [(urlparse.urlparse(p).netloc, p) for p in
    conf_managers])
