def render_GET(self, request):...
"""docstring"""
def on_request_finished(_):...
self.events_requests.remove(request)
self.events_requests.append(request)
request.notifyFinish().addCallbacks(on_request_finished, on_request_finished)
request.write(json.dumps({'type': 'events_start', 'event': {
    'tribler_started': self.session.lm.initComplete, 'version': version_id}
    }) + '\n')
return server.NOT_DONE_YET
