def __init__(self, profiler, event_type, extra_data=None):...
"""docstring"""
self.profiler = profiler
self.event_type = event_type
self.extra_data = extra_data if extra_data is not None else {}
