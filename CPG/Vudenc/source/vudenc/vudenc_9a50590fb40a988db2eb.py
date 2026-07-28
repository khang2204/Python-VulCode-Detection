from soscollector.clusters import Cluster
packages = 'kubernetes-master',
sos_plugins = ['kubernetes']
sos_plugin_options = {'kubernetes.all': 'on'}
cmd = 'kubectl'
option_list = [('label', '',
    'Filter node list to those with matching label'), ('role', '',
    'Filter node list to those with matching role')]
def get_nodes(self):...
self.cmd += ' get nodes'
if self.get_option('label'):
self.cmd += ' -l %s ' % self.get_option('label')
res = self.exec_master_cmd(self.cmd)
if res['status'] == 0:
nodes = []
packages = 'atomic-openshift',
roles = [x for x in self.get_option('role').split(',') if x]
sos_preset = 'ocp'
for nodeln in res['stdout'].splitlines()[1:]:
cmd = 'oc'
node = nodeln.split()
return nodes
if not roles:
nodes.append(node[0])
if node[2] in roles:
nodes.append(node[0])
