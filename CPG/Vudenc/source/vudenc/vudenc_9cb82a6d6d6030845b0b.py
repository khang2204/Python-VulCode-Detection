@staticmethod...
if not isinstance(task_id, int):
data = {}
task = db.view_task(task_id, details=True)
if task:
entry = task.to_dict()
return Exception('Task not found')
entry['guest'] = {}
if task.guest:
entry['guest'] = task.guest.to_dict()
entry['errors'] = []
for error in task.errors:
entry['errors'].append(error.message)
entry['sample'] = {}
if task.sample_id:
sample = db.view_sample(task.sample_id)
data['task'] = entry
entry['sample'] = sample.to_dict()
return data
