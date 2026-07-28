def rename(self, oldpath, newpath):...
"""docstring"""
old = self.getfile(oldpath)
if old == False:
new = self.getfile(newpath)
if new != False:
self.get_path(os.path.dirname(oldpath)).remove(old)
old[A_NAME] = os.path.basename(newpath)
self.get_path(os.path.dirname(newpath)).append(old)
return
