def call_later(self, delay_sec, callback):...
"""docstring"""
timer = None
def call_wrapper():...
if timer not in self._timers:
return
self._timers.remove(timer)
callback()
logging.exception('Timer callback failed')
if not self._timers_dying:
timer = threading.Timer(delay_sec, call_wrapper)
self._timers.append(timer)
timer.daemon = True
timer.start()
