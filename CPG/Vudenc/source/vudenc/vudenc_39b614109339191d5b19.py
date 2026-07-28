def mkfile(self, path, uid, gid, size, mode, ctime=None):...
"""docstring"""
if self.newcount > 10000:
return False
if ctime is None:
ctime = time.time()
dir = self.get_path(os.path.dirname(path))
outfile = os.path.basename(path)
if outfile in [x[A_NAME] for x in dir]:
dir.remove([x for x in dir if x[A_NAME] == outfile][0])
dir.append([outfile, T_FILE, uid, gid, size, mode, ctime, [], None, None])
self.newcount += 1
return True
