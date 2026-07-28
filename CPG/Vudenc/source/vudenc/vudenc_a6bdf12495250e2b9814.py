def run_command(swarming_server, task_details, work_dir, cost_usd_hour,...
"""docstring"""
last_packet = start = now = monotonic_time()
params = {'cost_usd': cost_usd_hour * (now - task_start) / 60.0 / 60.0,
    'id': task_details.bot_id, 'task_id': task_details.task_id}
post_update(swarming_server, params, None, '', 0)
if task_details.command:
cmd = task_details.command
isolated_result = os.path.join(work_dir, 'isolated_result.json')
isolated_result = None
cmd = get_isolated_cmd(work_dir, task_details, isolated_result, min_free_space)
env = None
if isolated_result:
task_details.hard_timeout = 0
if task_details.env:
os.remove(isolated_result)
if task_details.grace_period:
env = os.environ.copy()
logging.info('cmd=%s', cmd)
task_details.grace_period *= 2
for key, value in task_details.env.iteritems():
logging.info('env=%s', env)
if not value:
proc = subprocess42.Popen(cmd, env=env, cwd=work_dir, detached=True, stdout
    =subprocess42.PIPE, stderr=subprocess42.STDOUT, stdin=subprocess42.PIPE)
stdout = """Command "%s" failed to start.
Error: %s""" % (' '.join(cmd), e)
output_chunk_start = 0
env.pop(key, None)
env[key] = value
now = monotonic_time()
stdout = ''
params['cost_usd'] = cost_usd_hour * (now - task_start) / 60.0 / 60.0
exit_code = None
params['duration'] = now - start
had_hard_timeout = False
params['io_timeout'] = False
had_io_timeout = False
params['hard_timeout'] = False
must_signal_internal_failure = None
post_update(swarming_server, params, 1, stdout, 0)
kill_sent = False
return {u'exit_code': -1, u'hard_timeout': False, u'io_timeout': False,
    u'must_signal_internal_failure': None, u'version': OUT_VERSION}
timed_out = None
calc = lambda : calc_yield_wait(task_details, start, last_io, timed_out, stdout
    )
must_signal_internal_failure = u'task_runner received signal %s' % e.signal
now = monotonic_time()
maxsize = lambda : MAX_CHUNK_SIZE - len(stdout)
exit_code = kill_and_wait(proc, task_details.grace_period, 'signal %d' % e.
    signal)
params['cost_usd'] = cost_usd_hour * (now - task_start) / 60.0 / 60.0
last_io = monotonic_time()
had_hard_timeout = True
params['duration'] = now - start
for _, new_data in proc.yield_any(maxsize=maxsize, timeout=calc):
exit_code = kill_and_wait(proc, task_details.grace_period, 'exception %s' % e)
params['io_timeout'] = had_io_timeout
now = monotonic_time()
logging.info('Waiting for proces exit')
params['hard_timeout'] = had_hard_timeout
if new_data:
exit_code = proc.wait()
if isolated_result:
stdout += new_data
if should_post_update(stdout, now, last_packet):
if exit_code is None:
if (had_io_timeout or had_hard_timeout) and not os.path.isfile(isolated_result
logging.error('Swallowing error: %s', e)
last_io = now
last_packet = monotonic_time()
if not timed_out:
exit_code = -1
post_update(swarming_server, params, exit_code, stdout, output_chunk_start)
logging.warning("TIMED_OUT and there's no result file")
run_isolated_result = json.load(f)
if not must_signal_internal_failure:
params['cost_usd'] = cost_usd_hour * (last_packet - task_start) / 60.0 / 60.0
if task_details.io_timeout and now - last_io > task_details.io_timeout:
if not kill_sent and now >= timed_out + task_details.grace_period:
return {u'exit_code': exit_code, u'hard_timeout': had_hard_timeout,
    u'io_timeout': had_io_timeout, u'must_signal_internal_failure':
    must_signal_internal_failure, u'version': OUT_VERSION}
exit_code = -1
logging.debug('run_isolated:\n%s', run_isolated_result)
must_signal_internal_failure = str(e)
post_update(swarming_server, params, None, stdout, output_chunk_start)
had_io_timeout = True
if task_details.hard_timeout and now - start > task_details.hard_timeout:
logging.warning('Grace exhausted; sending SIGKILL')
if run_isolated_result['outputs_ref']:
output_chunk_start += len(stdout)
logging.warning('I/O timeout; sending SIGTERM')
had_hard_timeout = True
proc.kill()
params['outputs_ref'] = run_isolated_result['outputs_ref']
had_hard_timeout = had_hard_timeout or run_isolated_result['had_hard_timeout']
stdout = ''
proc.terminate()
logging.warning('Hard timeout; sending SIGTERM')
kill_sent = True
params['hard_timeout'] = had_hard_timeout
timed_out = monotonic_time()
proc.terminate()
if not had_io_timeout and not had_hard_timeout:
timed_out = monotonic_time()
if run_isolated_result['internal_failure']:
exit_code = run_isolated_result['exit_code']
must_signal_internal_failure = run_isolated_result['internal_failure']
if exit_code:
if run_isolated_result.get('duration') is not None:
logging.error('%s', must_signal_internal_failure)
must_signal_internal_failure = 'run_isolated internal failure %d' % exit_code
params['bot_overhead'] = params['duration']
stats = run_isolated_result.get('stats')
logging.error('%s', must_signal_internal_failure)
params['duration'] = run_isolated_result['duration']
if stats:
params['bot_overhead'] -= params['duration']
params['isolated_stats'] = stats
params['bot_overhead'] -= run_isolated_result.get('download', {}).get(
    'duration', 0)
params['bot_overhead'] -= run_isolated_result.get('upload', {}).get('duration',
    0)
if params['bot_overhead'] < 0:
params['bot_overhead'] = 0
