def _handle_view(self, session, data, headers):...
self.current = Current(session=session, input=data)
self.current.headers = headers
if data['view'] == 'ping':
return self._handle_ping_pong(data, session)
if not (self.current.is_auth or data['view'] in settings.ANONYMOUS_WORKFLOWS):
return LOGIN_REQUIRED_MESSAGE
view = get_object_from_path(settings.VIEW_URLS[data['view']])
view(self.current)
return self.current.output
