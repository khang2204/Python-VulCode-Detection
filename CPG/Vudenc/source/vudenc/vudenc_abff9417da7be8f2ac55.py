@property...
"""docstring"""
res = self.config.get(self.section, 'syslog_socket')
if not res:
res = None
return res
