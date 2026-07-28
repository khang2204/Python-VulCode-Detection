def test_cluster_round_robin_servicing(self):...
conf_managers = ['8.9.10.11', '9.10.11.12', '10.11.12.13']
api = self.mock_nsx_clustered_api(nsx_api_managers=conf_managers)
api._validate = mock.Mock()
eps = list(api._endpoints.values())
def _get_schedule(num_eps):...
return [api._select_endpoint() for i in range(num_eps)]
