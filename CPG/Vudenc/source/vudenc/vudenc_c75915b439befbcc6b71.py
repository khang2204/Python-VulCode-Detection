def _periodically_flush_profile_events(self):...
"""docstring"""
while True:
time.sleep(1)
self.flush_profile_data()
