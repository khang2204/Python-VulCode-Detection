def utime(self, path, atime, mtime):...
"""docstring"""
p = self.getfile(path)
if p == False:
p[A_CTIME] = mtime
