@command...
"""docstring"""
project_id = None
if self.state.active_project:
project_id = self.state.active_project.obj_id
if args:
pos = 0
project_id = args[0]
if project_id:
project = Project(project_id)
projects = wrapper.todoist.get_projects()
prnt('<', project, '>', VIOLET, None, VIOLET)
tasks = []
pos = cli.print_listing(project, pos)
for project in projects:
return project.tasks
prnt('<', project, '>', VIOLET, None, VIOLET)
return tasks
pos = cli.print_listing(project, pos)
tasks.extend(project.tasks)
