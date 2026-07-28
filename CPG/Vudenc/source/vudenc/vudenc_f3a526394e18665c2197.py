def connect_to_master(self):...
"""docstring"""
self.master = SosNode(self.config['master'], self.config)
self.log_debug('Failed to connect to master: %s' % e)
self._exit("""Could not connect to master node.
Aborting...""", 1)
