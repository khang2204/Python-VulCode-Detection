def close_all_connections(self):...
"""docstring"""
for client in self.client_list:
self.log_debug('Closing SSH connection to %s' % client.address)
client.close_ssh_session()
