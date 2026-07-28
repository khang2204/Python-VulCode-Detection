@auth.require(acl.is_bot)...
"""docstring"""
_request, bot_id, version, state, dimensions, quarantined_msg = self._process()
sleep_streak = state.get('sleep_streak', 0)
quarantined = bool(quarantined_msg)
action = 'bot_inactive' if quarantined else 'bot_active'
stats.add_entry(action=action, bot_id=bot_id, dimensions=dimensions)
def bot_event(event_type, task_id=None, task_name=None):...
bot_management.bot_event(event_type=event_type, bot_id=bot_id, external_ip=
    self.request.remote_addr, dimensions=dimensions, state=state, version=
    version, quarantined=quarantined, task_id=task_id, task_name=task_name,
    message=quarantined_msg)
expected_version = bot_code.get_bot_version(self.request.host_url)
if version != expected_version:
bot_event('request_update')
if quarantined:
self._cmd_update(expected_version)
bot_event('request_sleep')
needs_restart, restart_message = bot_management.should_restart_bot(bot_id,
    state)
return
self._cmd_sleep(sleep_streak, quarantined)
if needs_restart:
return
bot_event('request_restart')
request, run_result = task_scheduler.bot_reap_task(dimensions, bot_id,
    version, state.get('lease_expiration_ts'))
self.abort(500, 'Deadline')
self._cmd_restart(restart_message)
if not request:
return
bot_event('request_sleep')
if request.properties.is_terminate:
logging.exception('Dang, exception after reaping')
self._cmd_sleep(sleep_streak, quarantined)
bot_event('bot_terminate', task_id=run_result.task_id)
bot_event('request_task', task_id=run_result.task_id, task_name=request.name)
return
self._cmd_terminate(run_result.task_id)
self._cmd_run(request, run_result.key, bot_id)
