def mark_dnr_nodes(self):...
root_nodes = self.get_root_nodes()
nodes = copy.copy(root_nodes)
nodes_marked_do_not_run = []
node_ids_visited = set()
for index, n in enumerate(nodes):
obj = n['node_object']
return [n['node_object'] for n in nodes_marked_do_not_run]
if obj.id in node_ids_visited:
node_ids_visited.add(obj.id)
job = obj.job
if not job and obj.do_not_run is False and n not in root_nodes:
parent_nodes = [p['node_object'] for p in self.get_dependents(obj)]
if obj.do_not_run:
all_parents_dnr = True
children_success = self.get_dependencies(obj, 'success_nodes')
if job and job.status == 'failed':
for p in parent_nodes:
children_failed = self.get_dependencies(obj, 'failure_nodes')
children_failed = self.get_dependencies(obj, 'success_nodes')
if job and job.status == 'successful':
if not p.job and p.do_not_run is False:
if all_parents_dnr:
children_always = self.get_dependencies(obj, 'always_nodes')
nodes.extend(children_failed)
children_success = self.get_dependencies(obj, 'failure_nodes')
all_parents_dnr = False
obj.do_not_run = True
children_all = children_failed + children_always
nodes.extend(children_success)
nodes_marked_do_not_run.append(n)
nodes.extend(children_all)
