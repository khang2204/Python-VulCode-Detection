@property...
"""docstring"""
res = self.config.get(self.section, 'logdir')
if not res:
res = None
return res
