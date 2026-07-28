def __init__(self, config):...
os.umask(63)
self.config = config
self.client_list = []
self.node_list = []
self.master = False
self.retrieved = 0
self.need_local_sudo = False
self.clusters = self.config['cluster_types']
if not self.config['list_options']:
if not self.config['tmp_dir']:
self._exit('Exiting on user cancel', 130)
self.create_tmp_dir()
self._setup_logging()
self.log_debug('Executing %s' % ' '.join(s for s in sys.argv))
self.log_debug('Found cluster profiles: %s' % self.clusters.keys())
self.log_debug('Found supported host types: %s' % self.config['host_types']
    .keys())
self._parse_options()
self.prep()
