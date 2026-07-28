def get_path(self, path, follow_symlinks=True):...
"""docstring"""
cwd = self.fs
for part in path.split('/'):
if not len(part):
return cwd[A_CONTENTS]
ok = False
for c in cwd[A_CONTENTS]:
if c[A_NAME] == part:
if not ok:
if c[A_TYPE] == T_LINK:
cwd = self.getfile(c[A_TARGET], follow_symlinks=follow_symlinks)
cwd = c
ok = True
