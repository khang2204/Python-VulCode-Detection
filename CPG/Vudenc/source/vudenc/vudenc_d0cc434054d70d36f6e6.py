def get_nodes(self):...
self.cmd += ' get nodes'
if self.get_option('label'):
self.cmd += ' -l %s ' % self.get_option('label')
res = self.exec_master_cmd(self.cmd)
if res['status'] == 0:
nodes = []
roles = [x for x in self.get_option('role').split(',') if x]
for nodeln in res['stdout'].splitlines()[1:]:
node = nodeln.split()
return nodes
if not roles:
nodes.append(node[0])
if node[2] in roles:
nodes.append(node[0])
