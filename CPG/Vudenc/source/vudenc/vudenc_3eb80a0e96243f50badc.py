def draw_graph(self):...
deps = Digraph('Deps', strict=True)
deps.graph_attr.update(rankdir='BT')
node = self.nodes.get('master_node')
self.logger.error(
    'Detected circular dependency reference between %s and %s!' % (ex.node1,
    ex.node2))
deps.view()
for current in node.depends_on:
deps.edge(ex.node1, ex.node2, 'circular error', color='red')
deps.node(current.comp_name)
deps.edge(ex.node2, ex.node1, color='red')
res = []
unres = []
dep_resolve(current, res, unres)
for node in res:
if 'depends' in node.component:
for dep in node.component['depends']:
if dep not in self.nodes:
deps.node(dep, color='red')
if node.comp_name is not 'master_node':
deps.edge(node.comp_name, dep, 'missing', color='red')
deps.edge(node.comp_name, dep)
