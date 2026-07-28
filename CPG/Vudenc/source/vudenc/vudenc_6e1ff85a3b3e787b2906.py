def get_nodes_from_cluster(self):...
"""docstring"""
if self.config['cluster_type']:
nodes = self.config['cluster']._get_nodes()
self.log_debug('Node list: %s' % nodes)
return nodes
