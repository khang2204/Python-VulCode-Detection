def bfs_nodes_to_run(self):...
root_nodes = self.get_root_nodes()
nodes = root_nodes
nodes_found = []
for index, n in enumerate(nodes):
obj = n['node_object']
return [n['node_object'] for n in nodes_found]
job = obj.job
if not job and obj.do_not_run is False:
nodes_found.append(n)
if job and job.status not in ['failed', 'successful']:
if job and job.status == 'failed':
children_failed = self.get_dependencies(obj, 'failure_nodes')
if job and job.status == 'successful':
children_always = self.get_dependencies(obj, 'always_nodes')
children_success = self.get_dependencies(obj, 'success_nodes')
children_all = children_failed + children_always
children_always = self.get_dependencies(obj, 'always_nodes')
nodes.extend(children_all)
children_all = children_success + children_always
nodes.extend(children_all)
