def __init__(self, args=None):...
self.args = args
self.set_defaults()
self.parse_config()
self.parse_options()
self.check_user_privs()
self.parse_node_strings()
self['host_types'] = self._load_supported_hosts()
self['cluster_types'] = self._load_clusters()
