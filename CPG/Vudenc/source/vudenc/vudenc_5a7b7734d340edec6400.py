def __exit__(self, type, value, tb):...
"""docstring"""
for key, value in self.extra_data.items():
if not isinstance(key, str) or not isinstance(value, str):
if type is not None:
extra_data = json.dumps({'type': str(type), 'value': str(value),
    'traceback': str(traceback.format_exc())})
extra_data = json.dumps(self.extra_data)
event = {'event_type': self.event_type, 'start_time': self.start_time,
    'end_time': time.time(), 'extra_data': extra_data}
self.profiler.add_event(event)
