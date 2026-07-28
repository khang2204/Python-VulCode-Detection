def resolve_path_wc(self, path, cwd):...
"""docstring"""
pieces = path.rstrip('/').split('/')
if len(pieces[0]):
cwd = [x for x in cwd.split('/') if len(x) and x is not None]
cwd, pieces = [], pieces[1:]
path = path[1:]
found = []
def foo(p, cwd):...
if not len(p):
found.append('/%s' % ('/'.join(cwd),))
if p[0] == '.':
foo(pieces, cwd)
foo(p[1:], cwd)
if p[0] == '..':
return found
foo(p[1:], cwd[:-1])
names = [x[A_NAME] for x in self.get_path('/'.join(cwd))]
matches = [x for x in names if fnmatch.fnmatchcase(x, p[0])]
for match in matches:
foo(p[1:], cwd + [match])
