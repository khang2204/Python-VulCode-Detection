def new_mocked_cluster(self, conf_managers, validate_conn_func,...
mock_provider = mock.Mock()
mock_provider.default_scheme = 'https'
mock_provider.validate_connection = validate_conn_func
nsxlib_config = get_default_nsxlib_config()
if concurrent_connections:
nsxlib_config.concurrent_connections = concurrent_connections
nsxlib_config.http_provider = mock_provider
nsxlib_config.nsx_api_managers = conf_managers
return nsx_cluster.NSXClusteredAPI(nsxlib_config)
