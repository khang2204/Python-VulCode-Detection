def test(self, pathctx, levelctx):...
path_set = set(pathctx.parameters.keys())
extra_param = path_set - self._targetparam
extra_count = len(extra_param)
missing_count = len(self._targetparam - path_set)
testpath = fs.split_path(pathctx.path)
lenpath = min(self._lensplitpath, len(testpath))
if extra_count == 1 and not missing_count and levelctx.parameter:
key = extra_param.pop()
if not key in self._store:
self._store[key] = []
self._store[key].append(pathctx)
