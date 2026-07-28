def start_app(self, wait_time=APP_START_WAIT_TIME):...
"""docstring"""
self.check_app_installed()
self._do_start_app()
for _ in range(wait_time):
time.sleep(1)
if self._is_app_running():
self._log.debug('Successfully started %s', self.app_name)
return
