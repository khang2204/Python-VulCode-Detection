def call_wrapper():...
if timer not in self._timers:
return
self._timers.remove(timer)
callback()
logging.exception('Timer callback failed')
