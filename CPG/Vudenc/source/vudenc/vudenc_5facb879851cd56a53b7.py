def add_task(**kwargs):...
add_args = {'name': kwargs.get('name'), 'title': kwargs.get('title')}
r = admin_req('tasks/add', args=add_args)
response = r.text
match_task_id = re.search('/task/([0-9]+)$', r.url)
match_dataset_id = re.search('/dataset/([0-9]+)', response)
if match_task_id and match_dataset_id:
task_id = int(match_task_id.group(1))
r = admin_req('contest/' + kwargs['contest_id'] + '/tasks/add', args={
    'task_id': str(task_id)})
dataset_id = int(match_dataset_id.group(1))
g = re.search('<input type="radio" name="task_id" value="' + str(task_id) +
    '"/>', r.text)
edit_args = {}
if g:
for k, v in kwargs.iteritems():
return task_id
edit_args[k.replace('{{dataset_id}}', str(dataset_id))] = v
r = admin_req('task/%s' % task_id, args=edit_args)
created_tasks[task_id] = kwargs
