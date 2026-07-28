def init_honeyfs(self, honeyfs_path):...
"""docstring"""
for path, directories, filenames in os.walk(honeyfs_path):
for filename in filenames:
realfile_path = os.path.join(path, filename)
virtual_path = '/' + os.path.relpath(realfile_path, honeyfs_path)
f = self.getfile(virtual_path, follow_symlinks=False)
if f and f[A_TYPE] == T_FILE:
self.update_realfile(f, realfile_path)
