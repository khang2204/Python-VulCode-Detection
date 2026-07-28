@auth.require_xsrf_token_request...
_request, bot_id, version, state, dimensions, quarantined_msg = self._process()
bot_management.bot_event(event_type='bot_connected', bot_id=bot_id,
    external_ip=self.request.remote_addr, dimensions=dimensions, state=
    state, version=version, quarantined=bool(quarantined_msg), task_id='',
    task_name=None, message=quarantined_msg)
data = {'bot_version': bot_code.get_bot_version(self.request.host_url),
    'expiration_sec': auth.handler.XSRFToken.expiration_sec,
    'server_version': utils.get_app_version(), 'xsrf_token': self.
    generate_xsrf_token()}
self.send_response(data)
