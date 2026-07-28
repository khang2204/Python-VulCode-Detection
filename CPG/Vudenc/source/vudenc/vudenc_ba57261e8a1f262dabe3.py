def __init__(self, session_response=None, username=None, password=None,...
nsxlib_config = config.NsxLibConfig(username=username or NSX_USER, password
    =password or NSX_PASSWORD, retries=retries or NSX_HTTP_RETRIES,
    insecure=insecure if insecure is not None else NSX_INSECURE, ca_file=
    ca_file or NSX_CERT, concurrent_connections=concurrent_connections or
    NSX_CONCURENT_CONN, http_timeout=http_timeout or NSX_HTTP_TIMEOUT,
    http_read_timeout=http_read_timeout or NSX_HTTP_READ_TIMEOUT,
    conn_idle_timeout=conn_idle_timeout or NSX_CONN_IDLE_TIME,
    http_provider=NsxClientTestCase.MockHTTPProvider(session_response=
    session_response), nsx_api_managers=nsx_api_managers or [NSX_MANAGER],
    plugin_scope=PLUGIN_SCOPE, plugin_tag=PLUGIN_TAG, plugin_ver=PLUGIN_VER)
super(NsxClientTestCase.MockNSXClusteredAPI, self).__init__(nsxlib_config)
self._record = mock.Mock()
