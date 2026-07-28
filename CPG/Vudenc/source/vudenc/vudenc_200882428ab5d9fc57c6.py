def __init__(self, targetpath, client):...
self._splitpath = fs.split_path(targetpath)
self._lensplitpath = len(self._splitpath)
self._store = {}
self._ds = client
