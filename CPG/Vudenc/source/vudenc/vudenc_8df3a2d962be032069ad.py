def post_event(self, event_type, message):...
"""docstring"""
data = self._attributes.copy()
data['event'] = event_type
data['message'] = message
self._remote.url_read_json('/swarming/api/v1/bot/event', data=data)
