def get_nsxlib_config_with_client_cert():...
return config.NsxLibConfig(client_cert_provider=client_cert.
    ClientCertProvider(CLIENT_CERT), retries=NSX_HTTP_RETRIES, insecure=
    NSX_INSECURE, ca_file=NSX_CERT, concurrent_connections=
    NSX_CONCURENT_CONN, http_timeout=NSX_HTTP_TIMEOUT, http_read_timeout=
    NSX_HTTP_READ_TIMEOUT, conn_idle_timeout=NSX_CONN_IDLE_TIME,
    http_provider=None, nsx_api_managers=[], plugin_scope=PLUGIN_SCOPE,
    plugin_tag=PLUGIN_TAG, plugin_ver=PLUGIN_VER)
