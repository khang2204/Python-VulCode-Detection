def set_dependencies(self, exit_on_fail):...
for group in self.config['groups']:
for comp in group['components']:
master_node = Node({'name': 'master_node'})
self.nodes[comp['name']] = Node(comp)
for name in self.nodes:
node = self.nodes.get(name)
self.nodes['master_node'] = master_node
master_node.addEdge(node)
node = self.nodes.get('master_node')
self.logger.error(
    'Detected circular dependency reference between %s and %s!' % (ex.node1,
    ex.node2))
if 'depends' in node.component:
res = []
if exit_on_fail:
for dep in node.component['depends']:
unres = []
exit(1)
if dep in self.nodes:
dep_resolve(node, res, unres)
node.addEdge(self.nodes[dep])
self.logger.error("Unmet dependency: '%s' for component '%s'!" % (dep, node
    .comp_name))
dep_string = ''
if exit_on_fail:
for node in res:
exit(1)
if node is not master_node:
self.logger.debug('Dependency tree for start all: %s' % dep_string)
dep_string = '%s -> %s' % (dep_string, node.comp_name)
