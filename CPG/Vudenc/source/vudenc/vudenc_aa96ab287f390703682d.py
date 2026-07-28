def get_isolated_cmd(work_dir, task_details, isolated_result, min_free_space):...
"""docstring"""
bot_dir = os.path.dirname(work_dir)
if os.path.isfile(isolated_result):
os.remove(isolated_result)
cmd = get_run_isolated()
cmd.extend(['--isolated', task_details.inputs_ref['isolated'].encode(
    'utf-8'), '--namespace', task_details.inputs_ref['namespace'].encode(
    'utf-8'), '-I', task_details.inputs_ref['isolatedserver'].encode(
    'utf-8'), '--json', isolated_result, '--log-file', os.path.join(bot_dir,
    'logs', 'run_isolated.log'), '--cache', os.path.join(bot_dir, 'cache'),
    '--root-dir', os.path.join(work_dir, 'isolated')])
if min_free_space:
cmd.extend(('--min-free-space', str(min_free_space)))
if task_details.hard_timeout:
cmd.extend(('--hard-timeout', str(task_details.hard_timeout)))
if task_details.grace_period:
cmd.extend(('--grace-period', str(task_details.grace_period)))
if task_details.extra_args:
cmd.append('--')
return cmd
cmd.extend(task_details.extra_args)
