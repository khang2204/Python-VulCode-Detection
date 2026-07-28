def add_task_args(self, task):...
"""docstring"""
for t in ids_to_tasks(task).split(','):
agent = get_task_module(t)
if hasattr(agent, 'add_cmdline_args'):
agent.add_cmdline_args(self)
