@command...
"""docstring"""
sub_cmd = args[0]
if sub_cmd == 'create':
wrapper.todoist.create_project(args[1])
if sub_cmd == 'complete':
wrapper.todoist.complete_project(args[1])
if sub_cmd == 'clear':
wrapper.todoist.clear_project(args[1])
if sub_cmd == 'delete':
wrapper.todoist.delete_project(args[1])
