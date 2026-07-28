def __init__(self, workflow_job=None):...
super(WorkflowDAG, self).__init__()
if workflow_job:
self._init_graph(workflow_job)
