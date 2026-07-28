def load_and_run(in_file, swarming_server, cost_usd_hour, start, out_file,...
"""docstring"""
task_result = None
def handler(sig, _):...
logging.info('Got signal %s', sig)
work_dir = os.path.dirname(out_file)
if not os.path.isdir(work_dir):
if not task_result:
if not os.path.isdir(work_dir):
task_details = TaskDetails(json.load(f))
task_result = {u'exit_code': None, u'hard_timeout': False, u'io_timeout': 
    False, u'must_signal_internal_failure': 
    u'task_runner received signal %s' % e.signal, u'version': OUT_VERSION}
os.mkdir(work_dir)
json.dump(task_result, f)
task_result = run_command(swarming_server, task_details, work_dir,
    cost_usd_hour, start, min_free_space)
