def mkdir(self, path, uid, gid, size, mode, ctime=None):...
"""docstring"""
if self.newcount > 10000:
if ctime is None:
ctime = time.time()
if not len(path.strip('/')):
dir = self.get_path(os.path.dirname(path.strip('/')))
return False
dir.append([os.path.basename(path), T_DIR, uid, gid, size, mode, ctime, [],
    None, None])
self.newcount += 1
