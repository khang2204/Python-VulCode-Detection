def cancel_all_timers(self):...
"""docstring"""
timers = None
self._timers_dying = True
for t in self._timers:
t.cancel()
timers, self._timers = self._timers, []
for t in timers:
t.join(timeout=5)
if t.isAlive():
logging.error('Timer thread did not terminate fast enough: %s', t)
