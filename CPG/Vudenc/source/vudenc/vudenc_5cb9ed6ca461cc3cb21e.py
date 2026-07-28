def __init__(self, targetctx, client):...
self._splitpath = fs.split_path(targetctx.path)
self._targetparam = set(targetctx.parameters.keys())
self._lensplitpath = len(self._splitpath)
self._store = {}
self._ds = client
