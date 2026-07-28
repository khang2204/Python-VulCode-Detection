import copy
from awx.main.scheduler.dag_simple import SimpleDAG
def __init__(self, workflow_job=None):...
super(WorkflowDAG, self).__init__()
if workflow_job:
self._init_graph(workflow_job)
def _init_graph(self, workflow_job):...
node_qs = workflow_job.workflow_job_nodes
workflow_nodes = node_qs.prefetch_related('success_nodes', 'failure_nodes',
    'always_nodes').all()
for workflow_node in workflow_nodes:
self.add_node(workflow_node)
for node_type in ['success_nodes', 'failure_nodes', 'always_nodes']:
for workflow_node in workflow_nodes:
def bfs_nodes_to_run(self):...
related_nodes = getattr(workflow_node, node_type).all()
root_nodes = self.get_root_nodes()
for related_node in related_nodes:
nodes = root_nodes
self.add_edge(workflow_node, related_node, node_type)
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
