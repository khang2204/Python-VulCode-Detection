def test_conns_per_pool(self):...
conf_managers = ['8.9.10.11', '9.10.11.12:4433']
api = self.new_mocked_cluster(conf_managers, _validate_conn_up,
    concurrent_connections=11)
for ep_id, ep in api.endpoints.items():
self.assertEqual(ep.pool.max_size, 11)
