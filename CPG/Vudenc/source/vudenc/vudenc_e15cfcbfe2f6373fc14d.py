def _init_graph(self, workflow_job):...
node_qs = workflow_job.workflow_job_nodes
workflow_nodes = node_qs.prefetch_related('success_nodes', 'failure_nodes',
    'always_nodes').all()
for workflow_node in workflow_nodes:
self.add_node(workflow_node)
for node_type in ['success_nodes', 'failure_nodes', 'always_nodes']:
for workflow_node in workflow_nodes:
related_nodes = getattr(workflow_node, node_type).all()
for related_node in related_nodes:
self.add_edge(workflow_node, related_node, node_type)
