def terminate(self, *_):...
"""docstring"""
Daemon.terminate(self, *_)
if self._current_process is not None:
self._current_process.terminate()
