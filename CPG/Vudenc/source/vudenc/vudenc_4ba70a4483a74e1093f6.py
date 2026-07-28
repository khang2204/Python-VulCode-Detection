@auth.require(acl.is_bot)...
request = self.parse_body()
msg = log_unexpected_subset_keys(self.ACCEPTED_KEYS, self.REQUIRED_KEYS,
    request, self.request, 'bot', 'keys')
if msg:
self.abort_with_error(400, error=msg)
bot_id = request['id']
cost_usd = request['cost_usd']
task_id = request['task_id']
bot_overhead = request.get('bot_overhead')
duration = request.get('duration')
exit_code = request.get('exit_code')
hard_timeout = request.get('hard_timeout')
io_timeout = request.get('io_timeout')
isolated_stats = request.get('isolated_stats')
output = request.get('output')
output_chunk_start = request.get('output_chunk_start')
outputs_ref = request.get('outputs_ref')
if bool(isolated_stats) != (bot_overhead is not None):
ereporter2.log_request(request=self.request, source='server', category=
    'task_failure', message='Failed to update task: %s' % task_id)
run_result_key = task_pack.unpack_run_result_key(task_id)
self.abort_with_error(400, error=
    """Both bot_overhead and isolated_stats must be set simultaneously
bot_overhead: %s
isolated_stats: %s"""
     % (bot_overhead, isolated_stats))
performance_stats = None
if isolated_stats:
download = isolated_stats['download']
if output is not None:
upload = isolated_stats['upload']
if outputs_ref:
output = base64.b64decode(output)
logging.error("""Failed to decode output
%s
%r""", e, output)
performance_stats = task_result.PerformanceStats(bot_overhead=bot_overhead,
    isolated_download=task_result.IsolatedOperation(duration=download[
    'duration'], initial_number_items=download['initial_number_items'],
    initial_size=download['initial_size'], items_cold=base64.b64decode(
    download['items_cold']), items_hot=base64.b64decode(download[
    'items_hot'])), isolated_upload=task_result.IsolatedOperation(duration=
    upload['duration'], items_cold=base64.b64decode(upload['items_cold']),
    items_hot=base64.b64decode(upload['items_hot'])))
outputs_ref = task_request.FilesRef(**outputs_ref)
state = task_scheduler.bot_update_task(run_result_key=run_result_key,
    bot_id=bot_id, output=output, output_chunk_start=output_chunk_start,
    exit_code=exit_code, duration=duration, hard_timeout=hard_timeout,
    io_timeout=io_timeout, cost_usd=cost_usd, outputs_ref=outputs_ref,
    performance_stats=performance_stats)
ereporter2.log_request(request=self.request, source='server', category=
    'task_failure', message='Failed to update task: %s' % e)
self.send_response({'ok': True})
output = output.encode('ascii', 'replace')
if not state:
self.abort_with_error(400, error=str(e))
logging.error("""Failed to decode output
%s
%r""", e, output)
logging.info('Failed to update, please retry')
if state in (task_result.State.COMPLETED, task_result.State.TIMED_OUT):
logging.exception('Internal error: %s', e)
self.abort_with_error(500, error='Failed to update, please retry')
action = 'task_completed'
assert state == task_result.State.RUNNING, state
self.abort_with_error(500, error=str(e))
bot_management.bot_event(event_type=action, bot_id=bot_id, external_ip=self
    .request.remote_addr, dimensions=None, state=None, version=None,
    quarantined=None, task_id=task_id, task_name=None)
action = 'task_update'
