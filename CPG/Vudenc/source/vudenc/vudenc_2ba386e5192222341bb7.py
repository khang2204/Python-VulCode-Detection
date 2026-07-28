def _connect_to_node(self, node):...
"""docstring"""
client = SosNode(node, self.config)
if client.connected:
self.client_list.append(client)
client.close_ssh_session()
