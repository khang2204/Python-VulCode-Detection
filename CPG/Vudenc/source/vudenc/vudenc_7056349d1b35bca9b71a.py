def read(self):...
"""docstring"""
self.position += 1
if self.position < len(self.string):
self.char = self.string[self.position]
self.char = None
return self.char
