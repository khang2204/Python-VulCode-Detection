def get_parameters(self, key, levelctx, pathctxlist):...
if levelctx.collection:
coll = self._ds.get_collection(levelctx.collection)
return 'X',
return coll[0],
