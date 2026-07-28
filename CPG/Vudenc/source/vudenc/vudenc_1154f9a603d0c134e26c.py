@auth.require(acl.is_bot)...
request = self.parse_body()
bot_id = request.get('id')
task_id = request.get('task_id', '')
message = request.get('message', 'unknown')
bot_management.bot_event(event_type='task_error', bot_id=bot_id,
    external_ip=self.request.remote_addr, dimensions=None, state=None,
    version=None, quarantined=None, task_id=task_id, task_name=None,
    message=message)
line = (
    """Bot: https://%s/restricted/bot/%s
Task failed: https://%s/user/task/%s
%s"""
     % (app_identity.get_default_version_hostname(), bot_id, app_identity.
    get_default_version_hostname(), task_id, message))
ereporter2.log_request(self.request, source='bot', message=line)
msg = log_unexpected_keys(self.EXPECTED_KEYS, request, self.request, 'bot',
    'keys')
if msg:
self.abort_with_error(400, error=msg)
msg = task_scheduler.bot_kill_task(task_pack.unpack_run_result_key(task_id),
    bot_id)
if msg:
logging.error(msg)
self.send_response({})
self.abort_with_error(400, error=msg)
