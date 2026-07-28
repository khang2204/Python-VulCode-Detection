def _run(self):...
self.schedule(self.dologin)
self.schedule(self.wait_loop)
self.schedule(self.counter_ticker.tick)
self.perform_tasks()
self.log.error(e)
self.return_user()
self.log.warning(e)
self.log.exception(e)
