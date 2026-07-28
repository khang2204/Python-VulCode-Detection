def __init__(self, configfile=None):...
self.logger = logging.getLogger(__name__)
self.logger.setLevel(logging.DEBUG)
self.configfile = configfile
self.nodes = {}
self.server = []
self.host_list = []
if configfile:
self.load_config(configfile)
self.config = None
self.session_name = self.config['name']
dump(self.config, outfile, default_flow_style=False)
self.logger.debug('Loading config was successful')
self.server = Server()
if self.server.has_session(self.session_name):
self.session = self.server.find_where({'session_name': self.session_name})
self.logger.info('starting new session by name "%s" on server' % self.
    session_name)
self.logger.info('found running session by name "%s" on server' % self.
    session_name)
self.session = self.server.new_session(session_name=self.session_name,
    window_name='Main')
