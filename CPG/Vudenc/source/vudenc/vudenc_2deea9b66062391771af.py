def _Read(self, relpath, relative_to=None):...
if relative_to is None:
relative_to = self.server.top_level
assert not relpath.startswith(os.sep)
path = os.path.join(relative_to, relpath)
return fp.read()
