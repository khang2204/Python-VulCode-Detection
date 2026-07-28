def on_finished(self):...
"""docstring"""
if self.shutting_down:
return
self._logger.warning('Events connection dropped, attempting to reconnect')
self.failed_attempts = 0
self.connect_timer = QTimer()
self.connect_timer.setSingleShot(True)
self.connect_timer.timeout.connect(self.connect)
self.connect_timer.start(500)
