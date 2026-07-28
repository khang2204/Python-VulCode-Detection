def log_error(self, msg):...
"""docstring"""
caller = inspect.stack()[1][3]
lmsg = '[%s:%s] %s' % (self._hostname, caller, msg)
self.logger.error(lmsg)
self.console.error(self._fmt_msg(msg))
