def initialize_new_task_list(user_info, all_tasks):...
"""docstring"""
new_user = User(**user_info)
new_user.save()
user_id = new_user.id
for task in all_tasks.values():
task['user_id'] = user_id
return 'new user and tasks created'
new_task = Task(**task)
new_task.save()
