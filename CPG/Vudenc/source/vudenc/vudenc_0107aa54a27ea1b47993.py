def tearDown(self):...
super(TestNovaNetwork, self).tearDown()
if self.manager.clients_initialized:
if self.servers:
for server in self.servers:
self._delete_server(server)
LOG.debug(traceback.format_exc())
self.servers.remove(server)
LOG.debug('Server was already deleted.')
