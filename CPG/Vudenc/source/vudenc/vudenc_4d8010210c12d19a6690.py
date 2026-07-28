def search_paths(self, searchexpr):...
"""docstring"""
searcher = pathexpr.SearcherExists(self, searchexpr)
ctx = ds.PathTraversalContext({}, {}, self._root, {}, None, None, None)
rule = self._doc['rules']['ROOT']
ds._traverse(searcher, rule, ctx, self)
return searcher._store
