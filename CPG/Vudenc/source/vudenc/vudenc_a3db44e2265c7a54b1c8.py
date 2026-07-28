def test_conf_providers_no_scheme(self):...
conf_managers = ['8.9.10.11', '9.10.11.12:4433']
api = self.new_mocked_cluster(conf_managers, _validate_conn_up)
self._assert_providers(api, [(p, 'https://%s' % p) for p in conf_managers])
