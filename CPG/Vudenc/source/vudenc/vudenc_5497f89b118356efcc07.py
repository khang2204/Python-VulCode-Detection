def readlink(self, path):...
"""docstring"""
p = self.getfile(path, follow_symlinks=False)
if p == False:
if not p[A_MODE] & stat.S_IFLNK:
return p[A_TARGET]
