def _handle_job(self, session, data, headers):...
self.current = Current(session=session, input=data)
self.current.headers = headers
method = get_object_from_path(settings.BG_JOBS[data['job']])
method(self.current)
