def traverse(self, searcher):...
ctx = ds.PathTraversalContext({}, {}, self._root, {}, None, None, None)
rule = self._doc['rules']['ROOT']
client = self
return ds._traverse(searcher, rule, ctx, client)
