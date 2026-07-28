def _test_health(self, validate_fn, expected_health):...
conf_managers = ['8.9.10.11', '9.10.11.12']
api = self.new_mocked_cluster(conf_managers, validate_fn)
self.assertEqual(expected_health, api.health)
