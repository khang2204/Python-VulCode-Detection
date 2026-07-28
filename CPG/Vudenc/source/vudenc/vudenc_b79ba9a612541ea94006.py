@auth.require(acl.is_bot)...
request, bot_id, version, state, dimensions, quarantined_msg = self._process()
event = request.get('event')
if event not in ('bot_error', 'bot_rebooting', 'bot_shutdown'):
self.abort_with_error(400, error='Unsupported event type')
message = request.get('message')
bot_management.bot_event(event_type=event, bot_id=bot_id, external_ip=self.
    request.remote_addr, dimensions=dimensions, state=state, version=
    version, quarantined=bool(quarantined_msg), task_id=None, task_name=
    None, message=message)
if event == 'bot_error':
line = """Bot: https://%s/restricted/bot/%s
Bot error:
%s""" % (app_identity
    .get_default_version_hostname(), bot_id, message)
self.send_response({})
ereporter2.log_request(self.request, source='bot', message=line)
