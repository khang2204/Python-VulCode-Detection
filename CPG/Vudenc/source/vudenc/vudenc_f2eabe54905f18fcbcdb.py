def does_intersect_path(self, pathctx):...
testpath = fs.split_path(pathctx.path)
lentestpath = len(testpath)
lenpath = min(self._lensplitpath, lentestpath)
does_pass = self._splitpath[:lenpath
    ] == testpath and lentestpath <= self._lensplitpath
if does_pass and lentestpath not in self._store:
self._store[lentestpath] = []
return does_pass
