def add_testcase(task_id, num, input_file, output_file, public):...
files = [('input', input_file), ('output', output_file)]
args = {}
args['codename'] = '%03d' % num
if public:
args['public'] = '1'
dataset_id = get_task_active_dataset_id(task_id)
admin_req('dataset/%d/testcases/add' % dataset_id, files=files, args=args)
