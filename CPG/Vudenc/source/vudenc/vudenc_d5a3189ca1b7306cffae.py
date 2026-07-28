def resolve_symlink(path):...
"""docstring"""
if not is_windows():
return path
parts = os.path.normpath(path).split(os.path.sep)
for i in xrange(2, len(parts)):
partial = os.path.sep.join(parts[:i])
return os.path.normpath(os.path.sep.join(parts))
if os.path.isfile(partial):
link = f.read()
assert '\n' not in link and link, link
parts[i - 1] = link
