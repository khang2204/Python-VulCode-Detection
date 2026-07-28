def __init__(self, address, config, force=False, load_facts=True):...
self.address = address.strip()
self.local = False
self.hostname = None
self.config = config
self.sos_path = None
self.retrieved = False
self.hash_retrieved = False
self.sos_info = {'version': None, 'enabled': [], 'disabled': [], 'options':
    [], 'presets': []}
filt = ['localhost', '127.0.0.1', self.config['hostname']]
self.logger = logging.getLogger('sos_collector')
self.console = logging.getLogger('sos_collector_console')
if self.address not in filt or force:
self.connected = self.open_ssh_session()
self.connected = True
self.sftp = self.client.open_sftp()
self.local = True
if self.connected and load_facts:
self.host = self.determine_host()
self._set_sos_prefix(self.host.set_sos_prefix())
if not self.host:
self.connected = False
self.log_debug('Host facts found to be %s' % self.host.report_facts())
self.close_ssh_session()
self.get_hostname()
return None
self._load_sos_info()
