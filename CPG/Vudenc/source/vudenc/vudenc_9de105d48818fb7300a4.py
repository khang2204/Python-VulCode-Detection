def lexists(self, path):...
"""docstring"""
f = self.getfile(path, follow_symlinks=False)
if f is not False:
return True
