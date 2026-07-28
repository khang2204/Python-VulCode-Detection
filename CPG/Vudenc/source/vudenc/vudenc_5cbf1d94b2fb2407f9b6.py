def remove(self, path):...
"""docstring"""
p = self.getfile(path, follow_symlinks=False)
if p == False:
self.get_path(os.path.dirname(path)).remove(p)
return
