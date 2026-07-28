def add_manager(task_id, manager):...
args = {}
files = [('manager', manager)]
dataset_id = get_task_active_dataset_id(task_id)
admin_req('dataset/%d/managers/add' % dataset_id, files=files, args=args)
