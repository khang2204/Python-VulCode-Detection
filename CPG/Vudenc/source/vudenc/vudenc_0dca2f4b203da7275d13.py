def _path_allowed(self, path):...
for p in self.ALLOWED_PATHS:
if path.startswith(p):
return False
return True
