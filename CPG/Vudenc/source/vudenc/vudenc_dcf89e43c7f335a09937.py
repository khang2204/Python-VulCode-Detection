def file_contents(self, target):...
"""docstring"""
path = self.resolve_path(target, os.path.dirname(target))
if not path or not self.exists(path):
f = self.getfile(path)
if f[A_TYPE] == T_DIR:
if f[A_TYPE] == T_FILE and f[A_REALFILE]:
return open(f[A_REALFILE], 'rb').read()
if f[A_TYPE] == T_FILE and f[A_SIZE] == 0:
return ''
