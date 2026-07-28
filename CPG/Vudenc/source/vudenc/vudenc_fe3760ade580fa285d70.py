def make_todo_list(verified_user):...
"""docstring"""
todo_list = {}
todo_list['userInfo'] = verified_user.to_json()
all_tasks = todo_list['userInfo'].pop('tasks')
return all_tasks
