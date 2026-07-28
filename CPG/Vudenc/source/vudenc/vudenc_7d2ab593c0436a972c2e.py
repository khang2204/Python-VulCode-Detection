def start_flush_thread(self):...
t = threading.Thread(target=self._periodically_flush_profile_events, name=
    'ray_push_profiling_information')
t.daemon = True
t.start()
