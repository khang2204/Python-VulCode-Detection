def __exit__(self, type, value, traceback):...
if self.stack:
self.stack.close()
self.stack = None
