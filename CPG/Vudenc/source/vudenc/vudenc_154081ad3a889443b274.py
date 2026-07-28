def update_user_tasks(verified_user, all_tasks):...
"""docstring"""
user_id = verified_user.id
db_user_tasks = verified_user.tasks
db_user_task_ids = set([task.id for task in db_user_tasks])
for task_id, task in all_tasks.items():
if task_id in db_user_task_ids:
if len(db_user_task_ids) > 0:
print(db_user_task_ids)
task['user_id'] = user_id
for task_id in db_user_task_ids:
return 'new tasks updated & created'
db_user_task_ids.remove(task_id)
new_task = Task(**task)
task_to_delete = storage.get('Task', task_id)
verified_user.bm_update(task)
new_task.save()
task_to_delete.delete()
print('deleted task')
