def test(self, pathctx, levelctx):...
testpath = fs.split_path(pathctx.path)
lenpath = min(self._lensplitpath, len(testpath))
if self._splitpath[:lenpath] == testpath[:lenpath]:
self._store[lenpath].append(pathctx)
