def rmdir(self, path):...
"""docstring"""
path = path.rstrip('/')
name = os.path.basename(path)
parent = os.path.dirname(path)
dir = self.getfile(path, follow_symlinks=False)
if dir == False:
if dir[A_TYPE] != T_DIR:
if len(self.get_path(path)) > 0:
pdir = self.get_path(parent, follow_symlinks=True)
for i in pdir[:]:
if i[A_NAME] == name:
return False
pdir.remove(i)
return True
