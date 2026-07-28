def resolve_path(self, path, cwd):...
"""docstring"""
pieces = path.rstrip('/').split('/')
if path[0] == '/':
cwd = []
cwd = [x for x in cwd.split('/') if len(x) and x is not None]
while 1:
if not len(pieces):
piece = pieces.pop(0)
return '/%s' % ('/'.join(cwd),)
if piece == '..':
if len(cwd):
if piece in ('.', ''):
cwd.pop()
cwd.append(piece)
