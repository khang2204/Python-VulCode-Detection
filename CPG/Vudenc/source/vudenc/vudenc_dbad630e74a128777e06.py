def restart(self, message):...
"""docstring"""
self.post_event('bot_rebooting', message)
self.cancel_all_timers()
if self._shutdown_hook:
self._shutdown_hook(self)
logging.exception('shutdown hook failed: %s', e)
os_utilities.restart(message, timeout=15 * 60)
self.post_error('This host partition is bad; please fix the host')
self.post_error('Bot is stuck restarting for: %s' % message)
while True:
time.sleep(1)
