@property...
"""docstring"""
if self.name_space:
return '%s.%s' % (self.name_space, self.name)
return self.name
