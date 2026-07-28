def does_intersect_path(self, pathctx):...
testpath = fs.split_path(pathctx.path)
lentestpath = len(testpath)
lenpath = min(self._lensplitpath, lentestpath)
extra_count = len(set(pathctx.parameters.keys()) - self._targetparam)
return self._splitpath[:lenpath] == testpath[:lenpath] and extra_count < 2
