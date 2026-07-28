def _close(self):...
if self._owned:
if self._listenerthread != threading.current_thread():
self._conn.close()
self._listenerthread.join(timeout=1.0)
self._check_handlers()
if self._listenerthread.is_alive():
warnings.warn('session listener still running')
