def test_cluster_validate_with_exception(self):...
conf_managers = ['8.9.10.11', '9.10.11.12', '10.11.12.13']
api = self.new_mocked_cluster(conf_managers, _validate_conn_down)
self.assertEqual(3, len(api.endpoints))
self.assertRaises(nsxlib_exc.ServiceClusterUnavailable, api.get,
    'api/v1/transport-zones')
