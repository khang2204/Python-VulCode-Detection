def is_workflow_done(self):...
root_nodes = self.get_root_nodes()
nodes = root_nodes
is_failed = False
for index, n in enumerate(nodes):
obj = n['node_object']
return True, is_failed
job = obj.job
if obj.unified_job_template is None:
is_failed = True
if not job:
return False, False
children_success = self.get_dependencies(obj, 'success_nodes')
children_failed = self.get_dependencies(obj, 'failure_nodes')
children_always = self.get_dependencies(obj, 'always_nodes')
if not is_failed and job.status != 'successful':
children_all = children_success + children_failed + children_always
if job.status in ['canceled', 'error']:
for child in children_all:
if job.status == 'failed':
if child['node_object'].job:
nodes.extend(children_failed + children_always)
if job.status == 'successful':
nodes.extend(children_success + children_always)
return False, False
