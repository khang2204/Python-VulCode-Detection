def get_parameters(self, key, levelctx, pathctxlist):...
ret = set()
for pathctx in pathctxlist:
testpath = fs.split_path(pathctx.path)
return ret
lenpath = len(testpath)
if self._lensplitpath > lenpath:
ret.add(self._splitpath[lenpath])
