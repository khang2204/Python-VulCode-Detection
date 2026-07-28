def get_nodes(self):...
"""docstring"""
if not self.config['master'] and not self.config['cluster']:
msg = """Could not determine a cluster type and no list of nodes or master node was provided.
Aborting..."""
nodes = self.get_nodes_from_cluster()
self.log_debug('Error parsing node list: %s' % e)
if self.config['nodes']:
self._exit(msg)
if self.config['nodes']:
self.log_debug('Setting node list to --nodes option')
for node in self.config['nodes']:
if not self.config['master']:
for node in nodes:
self.node_list = nodes
self.node_list = self.config['nodes']
if any(i in node for i in '*\\?()/[]'):
host = self.config['hostname'].split('.')[0]
self.reduce_node_list()
if self.compare_node_to_regex(node):
for node in self.node_list:
if node not in self.node_list:
for node in self.node_list:
self.config['hostlen'] = len(max(self.node_list, key=len))
self.config['hostlen'] = len(self.config['master'])
self.node_list.append(node)
if any(i in node for i in ('*', '\\', '?', '(', ')', '/')):
self.log_debug('Force adding %s to node list' % node)
if host == node.split('.')[0]:
self.node_list.append(self.config['hostname'])
self.node_list.remove(node)
self.node_list.append(node)
self.node_list.remove(node)
