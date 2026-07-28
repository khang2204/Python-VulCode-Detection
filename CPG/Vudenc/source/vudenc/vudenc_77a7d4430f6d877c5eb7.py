def reduce_node_list(self):...
"""docstring"""
if self.config['hostname'] in self.node_list and self.config['no_local']:
self.node_list.remove(self.config['hostname'])
for i in self.config['ip_addrs']:
if i in self.node_list:
if self.config['master']:
self.node_list.remove(i)
for n in self.node_list:
self.node_list = list(set(n for n in self.node_list if n))
if n == self.master.hostname or n == self.config['master']:
self.log_debug('Node list reduced to %s' % self.node_list)
self.node_list.remove(n)
