def exists(self, path):...
"""docstring"""
f = self.getfile(path, follow_symlinks=True)
if f is not False:
return True
