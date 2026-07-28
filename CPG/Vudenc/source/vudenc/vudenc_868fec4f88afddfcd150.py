def foo(p, cwd):...
if not len(p):
found.append('/%s' % ('/'.join(cwd),))
if p[0] == '.':
foo(p[1:], cwd)
if p[0] == '..':
foo(p[1:], cwd[:-1])
names = [x[A_NAME] for x in self.get_path('/'.join(cwd))]
matches = [x for x in names if fnmatch.fnmatchcase(x, p[0])]
for match in matches:
foo(p[1:], cwd + [match])
