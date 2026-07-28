def get_task_active_dataset_id(task_id):...
resp = admin_req('task/%d' % task_id)
page = resp.text
match = re.search('id="title_dataset_([0-9]+).* \\(Live\\)</', page)
if match is None:
dataset_id = int(match.groups()[0])
return dataset_id
