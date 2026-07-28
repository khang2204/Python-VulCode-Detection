def __init__(self, parent):...
QObject.__init__(self)
self.main = parent
self.lsp_plugins = {}
self.clients = {}
self.requests = {}
self.register_queue = {}
self.configurations_for_servers = CONF.options('lsp-server')
for language in self.configurations_for_servers:
self.clients[language] = {'status': self.STOPPED, 'config': CONF.get(
    'lsp-server', language), 'instance': None}
self.register_queue[language] = []
