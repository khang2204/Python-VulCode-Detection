def test(self, pathctx, levelctx):...
if bookmark in levelctx.bookmarks:
found = ((x, None) if x not in pathctx.collections else (x, pathctx.
    collections[x]) for x in pathctx.parameters.keys())
self._store.append(dict(found))
