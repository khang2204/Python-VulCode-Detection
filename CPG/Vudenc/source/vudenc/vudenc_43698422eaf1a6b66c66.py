def getfile(self, path, follow_symlinks=True):...
"""docstring"""
if path == '/':
return self.fs
pieces = path.strip('/').split('/')
cwd = ''
p = self.fs
for piece in pieces:
if piece not in [x[A_NAME] for x in p[A_CONTENTS]]:
return p
return False
for x in p[A_CONTENTS]:
if x[A_NAME] == piece:
cwd = '/'.join((cwd, piece))
if piece == pieces[-1] and follow_symlinks == False:
p = x
if x[A_TYPE] == T_LINK:
if x[A_TARGET][0] == '/':
p = x
p = self.getfile(x[A_TARGET], follow_symlinks=follow_symlinks)
p = self.getfile('/'.join((cwd, x[A_TARGET])), follow_symlinks=follow_symlinks)
if p == False:
return False
