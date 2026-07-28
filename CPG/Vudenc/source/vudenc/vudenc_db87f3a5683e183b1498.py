def stat(self, path, follow_symlinks=True):...
"""docstring"""
if path == '/':
p = {A_TYPE: T_DIR, A_UID: 0, A_GID: 0, A_SIZE: 4096, A_MODE: 16877,
    A_CTIME: time.time()}
p = self.getfile(path, follow_symlinks=follow_symlinks)
if p == False:
return _statobj(p[A_MODE], 0, 0, 1, p[A_UID], p[A_GID], p[A_SIZE], p[
    A_CTIME], p[A_CTIME], p[A_CTIME])
