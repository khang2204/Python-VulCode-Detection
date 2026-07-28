def on_error(self, error, reschedule_on_err):...
self._logger.info('Got Tribler core error: %s' % error)
if error == QNetworkReply.ConnectionRefusedError:
if self.failed_attempts == 40:
self.failed_attempts += 1
if reschedule_on_err:
self.connect_timer = QTimer()
self.connect_timer.setSingleShot(True)
self.connect_timer.timeout.connect(self.connect)
self.connect_timer.start(500)
