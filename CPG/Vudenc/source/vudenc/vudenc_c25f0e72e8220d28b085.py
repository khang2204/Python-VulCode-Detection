@command...
"""docstring"""
sub_cmd = args[0]
if sub_cmd == 'create':
if self.state.active_project is None:
if sub_cmd == 'complete':
proj_id = self.state.active_project.obj_id
wrapper.todoist.complete_task(args[1])
self.do_tasks(str(self.state.active_project.obj_id))
wrapper.todoist.create_task(args[1], proj_id)
