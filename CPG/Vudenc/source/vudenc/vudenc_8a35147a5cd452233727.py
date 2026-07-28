def log_debug(self, msg):...
"""docstring"""
msg = self._sanitize_log_msg(msg)
caller = inspect.stack()[1][3]
msg = '[%s:%s] %s' % (self._hostname, caller, msg)
self.logger.debug(msg)
if self.config['verbose']:
self.console.debug(msg)
