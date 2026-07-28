@staticmethod...
db = Database()
tasks_files = db.list_tasks(limit=limit, offset=offset, category='file',
    not_status=TASK_PENDING)
tasks_urls = db.list_tasks(limit=limit, offset=offset, category='url',
    not_status=TASK_PENDING)
data = []
if tasks_files:
for task in tasks_files:
if tasks_urls:
new = task.to_dict()
for task in tasks_urls:
return data
new['sample'] = db.view_sample(new['sample_id']).to_dict()
new = task.to_dict()
filename = os.path.basename(new['target'])
if db.view_errors(task.id):
new.update({'filename': filename})
new['errors'] = True
data.append(new)
if db.view_errors(task.id):
new['errors'] = True
data.append(new)
