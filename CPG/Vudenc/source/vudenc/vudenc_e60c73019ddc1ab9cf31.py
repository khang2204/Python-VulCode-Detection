@property...
"""docstring"""
res = self.config.get(self.section, 'logfile')
if not res:
res = None
return res
