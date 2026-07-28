def log_debug(self, msg):...
"""docstring"""
caller = inspect.stack()[1][3]
msg = '[sos_collector:%s] %s' % (caller, msg)
self.logger.debug(msg)
if self.config['verbose']:
self.console.debug(msg)
