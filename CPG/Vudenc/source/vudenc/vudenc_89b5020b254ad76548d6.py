def chown(self, path, uid, gid):...
"""docstring"""
p = self.getfile(path)
if p == False:
if uid != -1:
p[A_UID] = uid
if gid != -1:
p[A_GID] = gid
