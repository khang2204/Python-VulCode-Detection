def log_info(self, msg):...
"""docstring"""
caller = inspect.stack()[1][3]
lmsg = '[%s:%s] %s' % (self._hostname, caller, msg)
self.logger.info(lmsg)
self.console.info(self._fmt_msg(msg))
